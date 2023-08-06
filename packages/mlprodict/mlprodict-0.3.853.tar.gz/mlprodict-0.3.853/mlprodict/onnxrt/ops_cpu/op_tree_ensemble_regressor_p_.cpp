// Inspired from 
// https://github.com/microsoft/onnxruntime/blob/master/onnxruntime/core/providers/cpu/ml/tree_ensemble_regressor.cc.

#if !defined(_CRT_SECURE_NO_WARNINGS)
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <vector>
#include <thread>
#include <iterator>

#ifndef SKIP_PYTHON
//#include <pybind11/iostream.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
//#include <numpy/arrayobject.h>

#if USE_OPENMP
#include <omp.h>
#endif

namespace py = pybind11;
#endif

#include "op_common_.hpp"

template<typename NTYPE>
class RuntimeTreeEnsembleRegressorP
{
    public:
        
        struct TreeNodeElementId
        {
            int64_t tree_id;
            int64_t node_id;
        };

        struct SparseValue
        {
            int64_t i;
            NTYPE value;
        };

        struct TreeNodeElement<NTYPE>
        {
            TreeNodeElementId id;
            int64_t feature_id;
            NTYPE value;
            NTYPE hitrates;
            NODE_MODE modes;
            TreeNodeElement<NTYPE> *truenode;
            TreeNodeElement<NTYPE> *falsenode;
            bool missing_tracks_true;

            std::vector<SparseValue> weights;
        };
        
        // tree_ensemble_regressor.h
        std::vector<NTYPE> base_values_;
        int64_t n_targets_;
        POST_EVAL_TRANSFORM post_transform_;
        AGGREGATE_FUNCTION aggregate_function_;
        std::vector<TreeNodeElement<NTYPE>> nodes_;
        std::vector<TreeNodeElement<NTYPE>*> roots_;

        int64_t max_tree_depth_;
        int64_t nbtrees_;
        bool same_mode_;
        const int64_t kOffset_ = 4000000000L;
    
    public:
        
        RuntimeTreeEnsembleRegressorP();
        ~RuntimeTreeEnsembleRegressorP();

        void init(
            const std::string &aggregate_function,
            py::array_t<NTYPE> base_values,
            int64_t n_targets,
            py::array_t<int64_t> nodes_falsenodeids,
            py::array_t<int64_t> nodes_featureids,
            py::array_t<NTYPE> nodes_hitrates,
            py::array_t<int64_t> nodes_missing_value_tracks_true,
            const std::vector<std::string>& nodes_modes,
            py::array_t<int64_t> nodes_nodeids,
            py::array_t<int64_t> nodes_treeids,
            py::array_t<int64_t> nodes_truenodeids,
            py::array_t<NTYPE> nodes_values,
            const std::string& post_transform,
            py::array_t<int64_t> target_ids,
            py::array_t<int64_t> target_nodeids,
            py::array_t<int64_t> target_treeids,
            py::array_t<NTYPE> target_weights
        );
        
        py::array_t<NTYPE> compute(py::array_t<NTYPE> X) const;

        void ProcessTreeNode(NTYPE* predictions, int64_t treeindex,
                             const NTYPE* x_data, int64_t feature_base,
                             unsigned char* has_predictions) const;
    
        std::string runtime_options();

        int omp_get_max_threads();
        
        py::array_t<int> debug_threshold(py::array_t<NTYPE> values) const;

        py::array_t<NTYPE> compute_tree_outputs(py::array_t<NTYPE> values) const;

    private:

        void compute_gil_free(const std::vector<int64_t>& x_dims, int64_t N, int64_t stride,
                              const py::array_t<NTYPE>& X, py::array_t<NTYPE>& Z) const;
};


template<typename NTYPE>
RuntimeTreeEnsembleRegressorP<NTYPE>::RuntimeTreeEnsembleRegressor() {
}


template<typename NTYPE>
RuntimeTreeEnsembleRegressorP<NTYPE>::~RuntimeTreeEnsembleRegressor() {
}


template<typename NTYPE>
std::string RuntimeTreeEnsembleRegressorP<NTYPE>::runtime_options() {
    std::string res;
#ifdef USE_OPENMP
    res += "OPENMP";
#endif
    return res;
}


template<typename NTYPE>
int RuntimeTreeEnsembleRegressorP<NTYPE>::omp_get_max_threads() {
#if USE_OPENMP
    return ::omp_get_max_threads();
#else
    return 1;
#endif
}


template<typename NTYPE>
void RuntimeTreeEnsembleRegressorP<NTYPE>::init(
            const std::string &aggregate_function,
            py::array_t<NTYPE> base_values,
            int64_t n_targets,
            py::array_t<int64_t> nodes_falsenodeids,
            py::array_t<int64_t> nodes_featureids,
            py::array_t<NTYPE> nodes_hitrates,
            py::array_t<int64_t> nodes_missing_value_tracks_true,
            const std::vector<std::string>& nodes_modes,
            py::array_t<int64_t> nodes_nodeids,
            py::array_t<int64_t> nodes_treeids,
            py::array_t<int64_t> nodes_truenodeids,
            py::array_t<NTYPE> nodes_values,
            const std::string& post_transform,
            py::array_t<int64_t> target_ids,
            py::array_t<int64_t> target_nodeids,
            py::array_t<int64_t> target_treeids,
            py::array_t<NTYPE> target_weights
    ) {
    aggregate_function_ = to_AGGREGATE_FUNCTION(aggregate_function);        
    array2vector(base_values_, base_values, NTYPE);
    n_targets_ = n_targets;

    std::vector<int64_t> nodes_treeids_;
    std::vector<int64_t> nodes_nodeids_;
    std::vector<int64_t> nodes_featureids_;
    std::vector<NTYPE> nodes_values_;
    std::vector<NTYPE> nodes_hitrates_;
    std::vector<NODE_MODE> nodes_modes_;
    std::vector<int64_t> nodes_truenodeids_;
    std::vector<int64_t> nodes_falsenodeids_;
    std::vector<int64_t> missing_tracks_true_;

    std::vector<int64_t> target_nodeids_;
    std::vector<int64_t> target_treeids_;
    std::vector<int64_t> target_ids_;
    std::vector<NTYPE> target_weights_;    
    
    array2vector(nodes_falsenodeids_, nodes_falsenodeids, int64_t);
    array2vector(nodes_featureids_, nodes_featureids, int64_t);
    array2vector(nodes_hitrates_, nodes_hitrates, NTYPE);
    array2vector(missing_tracks_true_, nodes_missing_value_tracks_true, int64_t);
    array2vector(nodes_truenodeids_, nodes_truenodeids, int64_t);
    //nodes_modes_names_ = nodes_modes;
    array2vector(nodes_nodeids_, nodes_nodeids, int64_t);
    array2vector(nodes_treeids_, nodes_treeids, int64_t);
    array2vector(nodes_truenodeids_, nodes_truenodeids, int64_t);
    array2vector(nodes_values_, nodes_values, NTYPE);
    array2vector(nodes_truenodeids_, nodes_truenodeids, int64_t);
    post_transform_ = to_POST_EVAL_TRANSFORM(post_transform);
    array2vector(target_ids_, target_ids, int64_t);
    array2vector(target_nodeids_, target_nodeids, int64_t);
    array2vector(target_treeids_, target_treeids, int64_t);
    array2vector(target_weights_, target_weights, NTYPE);

    // additional members
    nodes_modes_.resize(nodes_modes.size());
    same_mode_ = true;
    size_t fpos = -1;
    for(size_t i = 0; i < nodes_modes.size(); ++i) {
        nodes_modes_[i] = to_NODE_MODE(nodes_modes[i]);
        if (nodes_modes_[i] == NODE_MODE::LEAF)
            continue;
        if (fpos == -1) {
            fpos = i;
            continue;
        }
        if (nodes_modes_[i] != nodes_modes_[fpos])
            same_mode_ = false;
    }

    max_tree_depth_ = 1000;
    
    // filling nodes

    /*
    std::vector<TreeNodeElement<NTYPE>> nodes_;
    std::vector<TreeNodeElement<NTYPE>*> roots_;
    */
    nodes_.clear();
    roots_.clear();
    std::map<int64_t,size_t> idi;
    
    for (size_t i = 0; i < nodes_treeids_.size(); i++) {
        TreeNodeElement<NTYPE> node;
        node.id.tree_id = nodes_treeids_[i];
        node.id.node_id = nodes_nodeids_[i];
        node.feature_id = nodes_featureids_[i];
        node.value = nodes_values_[i];
        node.hitrates = nodes_hitrates_[i];
        node.mode = nodes_modes_[i];
        node.truenode = NULL; // nodes_truenodeids_[i];
        node.falsenode = NULL; // nodes_falsenodeids_[i];
        node.missing_tracks_true = nodes_missing_value_tracks_true[i] == 1;
        nodes_.push_back(node);
        idi[node.id.node_id] = i;
    }

    for(auto it = nodes_.begin(), size_t i=0; it != nodes_.end(); ++it, ++i) {
        if (node.mode == NODE_MODE::LEAF)
            continue;        
        it->truenode = &(nodes_[idi[nodes_truenodeids_[i]]);
        it->falsenode = &(nodes_[idi[nodes_falsenodeids_[i]]);
    }
    
    int64_t previous = -1;
    std::map<TreeNodeElementId,TreeNodeElement<NTYPE>*> id_pointer;
    for(auto it = nodes_.begin(), size_t i=0; it != nodes_.end(); ++it, ++i) {
        if ((previous == -1) || (previous != node.id.tree_id))
            roots_.push_back(it);
        previous = node.id.tree_id;
        id_pointer[node.id] = it;
    }
        
    TreeNodeElementId ind;
    SparseValue w;
    for (size_t i = 0; i < target_nodeids_.size(); i++) {
        ind.tree_id = target_treeids_[i];
        ind.node_id = target_nodeids_[i];
        w.i = target_ids_[i];
        w.value = target_weights_[i];
    }
    
    nbtrees_ = roots_.size();    
}


template<typename NTYPE>
py::array_t<NTYPE> RuntimeTreeEnsembleRegressorP<NTYPE>::compute(py::array_t<NTYPE> X) const {
    // const Tensor& X = *context->Input<Tensor>(0);
    // const TensorShape& x_shape = X.Shape();    
    std::vector<int64_t> x_dims;
    arrayshape2vector(x_dims, X);
    if (x_dims.size() != 2)
        throw std::runtime_error("X must have 2 dimensions.");

    // Does not handle 3D tensors
    bool xdims1 = x_dims.size() == 1;
    int64_t stride = xdims1 ? x_dims[0] : x_dims[1];  
    int64_t N = xdims1 ? 1 : x_dims[0];

    // Tensor* Y = context->Output(0, TensorShape({N}));
    // auto* Z = context->Output(1, TensorShape({N, class_count_}));
    py::array_t<NTYPE> Z(x_dims[0] * n_targets_);

    {
        py::gil_scoped_release release;
        compute_gil_free(x_dims, N, stride, X, Z);
    }
    return Z;
}


py::detail::unchecked_mutable_reference<float, 1> _mutable_unchecked1(py::array_t<float>& Z) {
    return Z.mutable_unchecked<1>();
}


py::detail::unchecked_mutable_reference<double, 1> _mutable_unchecked1(py::array_t<double>& Z) {
    return Z.mutable_unchecked<1>();
}


template<typename NTYPE>
void RuntimeTreeEnsembleRegressorP<NTYPE>::compute_gil_free(
                const std::vector<int64_t>& x_dims, int64_t N, int64_t stride,
                const py::array_t<NTYPE>& X, py::array_t<NTYPE>& Z) const {

    // expected primary-expression before ')' token
    auto Z_ = _mutable_unchecked1(Z); // Z.mutable_unchecked<(size_t)1>();
                    
    const NTYPE* x_data = X.data(0);

    if (n_targets_ == 1) {
      NTYPE origin = base_values_.size() == 1 ? base_values_[0] : 0.f;
      if (N == 1) {
        int64_t current_weight_0 = 0;
        NTYPE scores = 0;
        unsigned char has_scores = 0;
        //for each tree
        #ifdef USE_OPENMP
        #pragma omp parallel for
        #endif
        for (int64_t j = 0; j < nbtrees_; ++j) {
          ProcessTreeNode(&scores, roots_[j], x_data, current_weight_0, &has_scores);
        }
        NTYPE val = has_scores
                ? (aggregate_function_ == AGGREGATE_FUNCTION::AVERAGE
                    ? scores / roots_.size()
                    : scores) + origin
                : origin;
        *((NTYPE*)Z_.data(0)) = (post_transform_ == POST_EVAL_TRANSFORM::PROBIT) 
                                    ? ComputeProbit(val) : val;
      }
      else {
          #ifdef USE_OPENMP
          #pragma omp parallel for
          #endif
          for (int64_t i = 0; i < N; ++i)  //for each class
          {
            int64_t current_weight_0 = i * stride;
            NTYPE scores = 0;
            unsigned char has_scores = 0;
            //for each tree
            for (size_t j = 0; j < nb_trees_; ++j) {
              ProcessTreeNode(&scores, roots_[j], x_data, current_weight_0, &has_scores);
            }
            NTYPE val = has_scores
                    ? (aggregate_function_ == AGGREGATE_FUNCTION::AVERAGE
                        ? scores / roots_.size()
                        : scores) + origin
                    : origin;
            *((NTYPE*)Z_.data(i)) = (post_transform_ == POST_EVAL_TRANSFORM::PROBIT) 
                                        ? ComputeProbit(val) : val;
          }
      }
    }
    else {
      if (N == 1) {
        int64_t current_weight_0 = 0;
        std::vector<NTYPE> scores(n_targets_, (NTYPE)0);
        std::vector<unsigned char> has_scores(n_targets_, 0);
        //for each tree
        #ifdef USE_OPENMP
        #pragma omp parallel for
        #endif
        for (int64_t j = 0; j < nbtrees_; ++j) {
          ProcessTreeNode(scores.data(), roots_[j], x_data, current_weight_0, has_scores.data());
        }
        //find aggregate, could use a heap here if there are many classes
        std::vector<NTYPE> outputs;
        for (int64_t j = 0; j < n_targets_; ++j) {
          //reweight scores based on number of voters
          NTYPE val = base_values_.size() == (size_t)n_targets_ ? base_values_[j] : 0.f;
          if (has_scores[j]) {
            val += aggregate_function_ == AGGREGATE_FUNCTION::AVERAGE
                      ? scores[j] / roots_.size()
                      : scores[j];
          }
          outputs.push_back(val);
        }
        write_scores(outputs, post_transform_, (NTYPE*)Z_.data(0), -1);
      }
      else {
          #ifdef USE_OPENMP
          #pragma omp parallel for
          #endif
          for (int64_t i = 0; i < N; ++i)  //for each class
          {
            int64_t current_weight_0 = i * stride;
            std::vector<NTYPE> scores(n_targets_, (NTYPE)0);
            std::vector<unsigned char> has_scores(n_targets_, 0);
            //for each tree
            for (size_t j = 0; j < roots_.size(); ++j) {
              ProcessTreeNode(scores.data(), roots_[j], x_data, current_weight_0, has_scores.data());
            }
            //find aggregate, could use a heap here if there are many classes
            std::vector<NTYPE> outputs;
            for (int64_t j = 0; j < n_targets_; ++j) {
              //reweight scores based on number of voters
              NTYPE val = base_values_.size() == (size_t)n_targets_ ? base_values_[j] : 0.f;
              if (has_scores[j]) {
                val += aggregate_function_ == AGGREGATE_FUNCTION::AVERAGE
                          ? scores[j] / roots_.size()
                          : scores[j];
              }
              outputs.push_back(val);
            }
            write_scores(outputs, post_transform_, (NTYPE*)Z_.data(i * n_targets_), -1);
          }
      }
    }
}


#define TREE_FIND_VALUE(CMP) \
    if (missing_tracks_true_.size() == nodes_truenodeids_.size()) { \
      while (mode != NODE_MODE::LEAF && loopcount >= 0) { \
        val = x_data[feature_base + nodes_featureids_[treeindex]]; \
        treeindex = root + \
            ((val CMP nodes_values_[treeindex] || \
                (missing_tracks_true_[treeindex] && std::isnan(static_cast<NTYPE>(val)))) \
              ? nodes_truenodeids_[treeindex] \
              : nodes_falsenodeids_[treeindex]); \
        mode = nodes_modes_[treeindex]; \
        --loopcount; \
      } \
    } \
    else { \
      while (mode != NODE_MODE::LEAF && loopcount >= 0) { \
        val = x_data[feature_base + nodes_featureids_[treeindex]]; \
        treeindex = root + (val CMP nodes_values_[treeindex] \
                              ? nodes_truenodeids_[treeindex] \
                              : nodes_falsenodeids_[treeindex]); \
        mode = nodes_modes_[treeindex]; \
        --loopcount; \
      } \
    }


#define TARGET_ASSIGN_LOOP(AFF) \
    int64_t dim_id; \
    NTYPE weight; \
    int64_t nodes_treeid = nodes_treeids_[treeindex]; \
    int64_t nodes_nodeid = nodes_nodeids_[treeindex]; \
    int64_t treeid = std::get<0>(*leaf); \
    int64_t nodeid = std::get<1>(*leaf); \
    while (treeid == nodes_treeid && nodeid == nodes_nodeid) { \
      dim_id = std::get<2>(*leaf); \
      weight = std::get<3>(*leaf); \
      AFF \
      ++index; \
      if (index >= leafnode_data_.size()) \
        break; \
      leaf = (std::tuple<int64_t, int64_t, int64_t, NTYPE>*) &(leafnode_data_[index]); \
      treeid = std::get<0>(*leaf); \
      nodeid = std::get<1>(*leaf); \
    }


template<typename NTYPE>
void RuntimeTreeEnsembleRegressorP<NTYPE>::ProcessTreeNode(
        NTYPE* predictions,
        int64_t treeindex, const NTYPE* x_data, int64_t feature_base,
        unsigned char* has_predictions) const {
  auto mode = nodes_modes_[treeindex];
  int64_t root = treeindex;
  bool tracktrue;
  NTYPE val;

  if (same_mode_) {
      int64_t loopcount = max_tree_depth_;
      switch(mode) {
        case NODE_MODE::BRANCH_LEQ:
          TREE_FIND_VALUE(<=)
          break;
        case NODE_MODE::BRANCH_LT:
          TREE_FIND_VALUE(<)
          break;
        case NODE_MODE::BRANCH_GTE:
          TREE_FIND_VALUE(>=)
          break;
        case NODE_MODE::BRANCH_GT:
          TREE_FIND_VALUE(>)
          break;
        case NODE_MODE::BRANCH_EQ:
          TREE_FIND_VALUE(==)
          break;
        case NODE_MODE::BRANCH_NEQ:
          TREE_FIND_VALUE(!=)
          break;
        case NODE_MODE::LEAF:
          break;
        default:
        {
          std::ostringstream err_msg;
          err_msg << "Invalid mode of value: " << static_cast<std::underlying_type<NODE_MODE>::type>(mode);
          throw std::runtime_error(err_msg.str());
        }
      }
  }
  else {  // Different rules to compare to node thresholds.
    int64_t loopcount = 0;
    while ((mode != NODE_MODE::LEAF && loopcount <= max_tree_depth_)) {
      NTYPE val = x_data[feature_base + nodes_featureids_[treeindex]];
      tracktrue = missing_tracks_true_.size() == nodes_truenodeids_.size() &&
                  missing_tracks_true_[treeindex] &&
                  std::isnan(static_cast<NTYPE>(val));
      NTYPE threshold = nodes_values_[treeindex];
      switch (mode) {
        case NODE_MODE::BRANCH_LEQ:
          treeindex = val <= threshold || tracktrue
                      ? nodes_truenodeids_[treeindex]
                      : nodes_falsenodeids_[treeindex];
          break;
        case NODE_MODE::BRANCH_LT:
          treeindex = val < threshold || tracktrue
                      ? nodes_truenodeids_[treeindex]
                      : nodes_falsenodeids_[treeindex];
          break;
        case NODE_MODE::BRANCH_GTE:
          treeindex = val >= threshold || tracktrue
                      ? nodes_truenodeids_[treeindex]
                      : nodes_falsenodeids_[treeindex];
          break;
        case NODE_MODE::BRANCH_GT:
          treeindex = val > threshold || tracktrue
                      ? nodes_truenodeids_[treeindex]
                      : nodes_falsenodeids_[treeindex];
          break;
        case NODE_MODE::BRANCH_EQ:
          treeindex = val == threshold || tracktrue
                      ? nodes_truenodeids_[treeindex]
                      : nodes_falsenodeids_[treeindex];
          break;
        case NODE_MODE::BRANCH_NEQ:
          treeindex = val != threshold || tracktrue
                      ? nodes_truenodeids_[treeindex]
                      : nodes_falsenodeids_[treeindex];
          break;
        default: {
          std::ostringstream err_msg;
          err_msg << "Invalid mode of value: " << static_cast<std::underlying_type<NODE_MODE>::type>(mode);
          throw std::runtime_error(err_msg.str());
        }
      }
      treeindex += root;
      mode = nodes_modes_[treeindex];
      ++loopcount;
    }      
  }

  //should be at leaf
  int64_t id = nodes_treeids_[treeindex] * kOffset_ + nodes_nodeids_[treeindex];
  //auto it_lp = leafdata_map.find(id);
  auto it_lp = leafdata_map_.find(id);
  if (it_lp != leafdata_map_.end()) {
    size_t index = it_lp->second;
    std::tuple<int64_t, int64_t, int64_t, NTYPE>* leaf = 
        (std::tuple<int64_t, int64_t, int64_t, NTYPE>*) &(leafnode_data_[index]);
      
    switch(aggregate_function_) {
      case AGGREGATE_FUNCTION::AVERAGE:
      case AGGREGATE_FUNCTION::SUM:
        if (consecutive_leaf_data_) {
            TARGET_ASSIGN_LOOP(has_predictions[dim_id] = 1; predictions[dim_id] += weight;)
        }
        else {
            int64_t dim_id = std::get<2>(*leaf);
            has_predictions[dim_id] = 1;
            predictions[dim_id] += std::get<3>(*leaf);
        }
        break;
      case AGGREGATE_FUNCTION::MIN:
        if (consecutive_leaf_data_) {
            TARGET_ASSIGN_LOOP(if (has_predictions[dim_id]) { if (weight < predictions[dim_id]) predictions[dim_id] = weight; } else { has_predictions[dim_id] = 1; predictions[dim_id] = weight; })
        }
        else {
          int64_t dim_id = std::get<2>(*leaf);
          NTYPE weight = std::get<3>(*leaf);
          if (has_predictions[dim_id]) {
            if (weight < predictions[dim_id])
              predictions[dim_id] = weight;
          }
          else {
            has_predictions[dim_id] = 1;
            predictions[dim_id] = weight;
          }
        }
        break;
      case AGGREGATE_FUNCTION::MAX:
        if (consecutive_leaf_data_) {
            TARGET_ASSIGN_LOOP(if (has_predictions[dim_id]) { if (weight > predictions[dim_id]) predictions[dim_id] = weight; } else { has_predictions[dim_id] = 1; predictions[dim_id] = weight; })
        }
        else {
          int64_t dim_id = std::get<2>(*leaf);
          NTYPE weight = std::get<3>(*leaf);
          if (has_predictions[dim_id]) {
            if (weight > predictions[dim_id])
              predictions[dim_id] = weight;
          }
          else {
            has_predictions[dim_id] = 1;
            predictions[dim_id] = weight;
          }
        }
        break;
    }
  }
}


template<typename NTYPE>
py::array_t<int> RuntimeTreeEnsembleRegressorP<NTYPE>::debug_threshold(py::array_t<NTYPE> values) const {
    std::vector<int> result(values.size() * nodes_values_.size());
    const NTYPE* x_data = values.data(0);
    const NTYPE* end = x_data + values.size();
    const NTYPE* pv;
    auto itb = result.begin();
    for(auto it = nodes_values_.begin(); it != nodes_values_.end(); ++it)
        for(pv=x_data; pv != end; ++pv, ++itb)
            *itb = *pv <= *it ? 1 : 0;
    std::vector<ssize_t> shape = { (ssize_t)nodes_values_.size(), values.size() };
    std::vector<ssize_t> strides = { (ssize_t)(values.size()*sizeof(int)),
                                     (ssize_t)sizeof(int) };
    return py::array_t<bool>(
        py::buffer_info(
            &result[0],
            sizeof(int),
            py::format_descriptor<int>::format(),
            2,
            shape,                                   /* shape of the matrix       */
            strides                                  /* strides for each axis     */
        ));
}


template<typename NTYPE>
py::array_t<NTYPE> RuntimeTreeEnsembleRegressorP<NTYPE>::compute_tree_outputs(py::array_t<NTYPE> X) const {
    
    std::vector<int64_t> x_dims;
    arrayshape2vector(x_dims, X);
    if (x_dims.size() != 2)
        throw std::runtime_error("X must have 2 dimensions.");

    int64_t stride = x_dims.size() == 1 ? x_dims[0] : x_dims[1];  
    int64_t N = x_dims.size() == 1 ? 1 : x_dims[0];
    
    std::vector<NTYPE> result(N * roots_.size());
    const NTYPE* x_data = X.data(0);
    auto itb = result.begin();

    for (int64_t i=0; i < N; ++i)  //for each class
    {
        int64_t current_weight_0 = i * stride;
        for (size_t j = 0; j < roots_.size(); ++j, ++itb) {
            std::vector<NTYPE> scores(n_targets_, (NTYPE)0);
            std::vector<unsigned char> has_scores(n_targets_, 0);
            ProcessTreeNode(scores.data(), roots_[j], x_data,
                            current_weight_0, has_scores.data());
            *itb = scores[0];
        }
    }
    
    std::vector<ssize_t> shape = { (ssize_t)N, (ssize_t)roots_.size() };
    std::vector<ssize_t> strides = { (ssize_t)(roots_.size()*sizeof(NTYPE)),
                                     (ssize_t)sizeof(NTYPE) };
    return py::array_t<bool>(
        py::buffer_info(
            &result[0],
            sizeof(NTYPE),
            py::format_descriptor<NTYPE>::format(),
            2,
            shape,                                   /* shape of the matrix       */
            strides                                  /* strides for each axis     */
        ));
}


class RuntimeTreeEnsembleRegressorFloat : public RuntimeTreeEnsembleRegressor<float>
{
    public:
        RuntimeTreeEnsembleRegressorFloat() : RuntimeTreeEnsembleRegressor<float>() {}
};


class RuntimeTreeEnsembleRegressorDouble : public RuntimeTreeEnsembleRegressor<double>
{
    public:
        RuntimeTreeEnsembleRegressorDouble() : RuntimeTreeEnsembleRegressor<double>() {}
};


#ifndef SKIP_PYTHON

PYBIND11_MODULE(op_tree_ensemble_regressor_, m) {
	m.doc() =
    #if defined(__APPLE__)
    "Implements runtime for operator TreeEnsembleRegressor."
    #else
    R"pbdoc(Implements runtime for operator TreeEnsembleRegressor. The code is inspired from
`tree_ensemble_regressor.cc <https://github.com/microsoft/onnxruntime/blob/master/onnxruntime/core/providers/cpu/ml/tree_ensemble_Regressor.cc>`_
in :epkg:`onnxruntime`.)pbdoc"
    #endif
    ;

    py::class_<RuntimeTreeEnsembleRegressorFloat> clf (m, "RuntimeTreeEnsembleRegressorFloat",
        R"pbdoc(Implements float runtime for operator TreeEnsembleRegressor. The code is inspired from
`tree_ensemble_regressor.cc <https://github.com/microsoft/onnxruntime/blob/master/onnxruntime/core/providers/cpu/ml/tree_ensemble_Regressor.cc>`_
in :epkg:`onnxruntime`. Supports float only.)pbdoc");

    clf.def(py::init<>());
    clf.def_readonly("roots_", &RuntimeTreeEnsembleRegressorFloat::roots_,
                     "Returns the roots indices.");
    clf.def("init", &RuntimeTreeEnsembleRegressorFloat::init,
            "Initializes the runtime with the ONNX attributes in alphabetical order.");
    clf.def("compute", &RuntimeTreeEnsembleRegressorFloat::compute,
            "Computes the predictions for the random forest.");
    clf.def("runtime_options", &RuntimeTreeEnsembleRegressorFloat::runtime_options,
            "Returns indications about how the runtime was compiled.");
    clf.def("omp_get_max_threads", &RuntimeTreeEnsembleRegressorFloat::omp_get_max_threads,
            "Returns omp_get_max_threads from openmp library.");

    clf.def_readonly("nodes_treeids_", &RuntimeTreeEnsembleRegressorFloat::nodes_treeids_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_readonly("nodes_nodeids_", &RuntimeTreeEnsembleRegressorFloat::nodes_nodeids_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_readonly("nodes_featureids_", &RuntimeTreeEnsembleRegressorFloat::nodes_featureids_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_readonly("nodes_values_", &RuntimeTreeEnsembleRegressorFloat::nodes_values_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_readonly("nodes_hitrates_", &RuntimeTreeEnsembleRegressorFloat::nodes_hitrates_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_property_readonly("nodes_modes_", [](RuntimeTreeEnsembleRegressorFloat* op) -> const py::array_t<int> {
        std::vector<int> i_nodes_modes(op->nodes_modes_.size());
        for(int i = 0; i < i_nodes_modes.size(); ++i)
            i_nodes_modes[i] = (int)op->nodes_modes_[i];
        return py::array_t<int>(
            py::buffer_info(
                &i_nodes_modes[0],
                sizeof(int),
                py::format_descriptor<int>::format(),
                1,
                { (ssize_t)i_nodes_modes.size() },  /* shape of the matrix       */
                { (ssize_t)sizeof(int) }            /* strides for each axis     */
            ));
    });    
    clf.def_readonly("nodes_truenodeids_", &RuntimeTreeEnsembleRegressorFloat::nodes_truenodeids_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_readonly("nodes_falsenodeids_", &RuntimeTreeEnsembleRegressorFloat::nodes_falsenodeids_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_readonly("missing_tracks_true_", &RuntimeTreeEnsembleRegressorFloat::missing_tracks_true_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_readonly("target_nodeids_", &RuntimeTreeEnsembleRegressorFloat::target_nodeids_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_readonly("target_treeids_", &RuntimeTreeEnsembleRegressorFloat::target_treeids_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_readonly("target_ids_", &RuntimeTreeEnsembleRegressorFloat::target_ids_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_readonly("target_weights_", &RuntimeTreeEnsembleRegressorFloat::target_weights_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_readonly("base_values_", &RuntimeTreeEnsembleRegressorFloat::base_values_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_readonly("n_targets_", &RuntimeTreeEnsembleRegressorFloat::n_targets_, "See :ref:`lpyort-TreeEnsembleRegressor`.");
    clf.def_readonly("post_transform_", &RuntimeTreeEnsembleRegressorFloat::post_transform_, "See :ref:`lpyort-TreeEnsembleRegressor`.");

    clf.def("debug_threshold", &RuntimeTreeEnsembleRegressorFloat::debug_threshold,
        "Checks every features against every features against every threshold. Returns a matrix of boolean.");
    clf.def("compute_tree_outputs", &RuntimeTreeEnsembleRegressorFloat::compute_tree_outputs,
        "Computes every tree output.");
    clf.def_readonly("same_mode_", &RuntimeTreeEnsembleRegressorFloat::same_mode_, "Tells if all nodes applies the same rule for thresholds.");
    clf.def_readonly("consecutive_leaf_data_", &RuntimeTreeEnsembleRegressorFloat::consecutive_leaf_data_,
        "Tells if there are two consecutive targets sharing the same node and the same tree (it should not happen in 1D target).");
        

    py::class_<RuntimeTreeEnsembleRegressorDouble> cld (m, "RuntimeTreeEnsembleRegressorDouble",
        R"pbdoc(Implements double runtime for operator TreeEnsembleRegressor. The code is inspired from
`tree_ensemble_regressor.cc <https://github.com/microsoft/onnxruntime/blob/master/onnxruntime/core/providers/cpu/ml/tree_ensemble_Regressor.cc>`_
in :epkg:`onnxruntime`. Supports double only.)pbdoc");

    cld.def(py::init<>());
    cld.def_readonly("roots_", &RuntimeTreeEnsembleRegressorDouble::roots_,
                     "Returns the roots indices.");
    cld.def("init", &RuntimeTreeEnsembleRegressorDouble::init,
            "Initializes the runtime with the ONNX attributes in alphabetical order.");
    cld.def("compute", &RuntimeTreeEnsembleRegressorDouble::compute,
            "Computes the predictions for the random forest.");
    cld.def("runtime_options", &RuntimeTreeEnsembleRegressorDouble::runtime_options,
            "Returns indications about how the runtime was compiled.");
    cld.def("omp_get_max_threads", &RuntimeTreeEnsembleRegressorDouble::omp_get_max_threads,
            "Returns omp_get_max_threads from openmp library.");

    cld.def_readonly("nodes_treeids_", &RuntimeTreeEnsembleRegressorDouble::nodes_treeids_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_readonly("nodes_nodeids_", &RuntimeTreeEnsembleRegressorDouble::nodes_nodeids_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_readonly("nodes_featureids_", &RuntimeTreeEnsembleRegressorDouble::nodes_featureids_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_readonly("nodes_values_", &RuntimeTreeEnsembleRegressorDouble::nodes_values_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_readonly("nodes_hitrates_", &RuntimeTreeEnsembleRegressorDouble::nodes_hitrates_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_property_readonly("nodes_modes_", [](RuntimeTreeEnsembleRegressorDouble* op) -> const py::array_t<int> {
        std::vector<int> i_nodes_modes(op->nodes_modes_.size());
        for(int i = 0; i < i_nodes_modes.size(); ++i)
            i_nodes_modes[i] = (int)op->nodes_modes_[i];
        return py::array_t<int>(
            py::buffer_info(
                &i_nodes_modes[0],
                sizeof(int),
                py::format_descriptor<int>::format(),
                1,
                { (ssize_t)i_nodes_modes.size() },  /* shape of the matrix       */
                { (ssize_t)sizeof(int) }            /* strides for each axis     */
            ));
    });    
    cld.def_readonly("nodes_truenodeids_", &RuntimeTreeEnsembleRegressorDouble::nodes_truenodeids_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_readonly("nodes_falsenodeids_", &RuntimeTreeEnsembleRegressorDouble::nodes_falsenodeids_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_readonly("missing_tracks_true_", &RuntimeTreeEnsembleRegressorDouble::missing_tracks_true_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_readonly("target_nodeids_", &RuntimeTreeEnsembleRegressorDouble::target_nodeids_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_readonly("target_treeids_", &RuntimeTreeEnsembleRegressorDouble::target_treeids_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_readonly("target_ids_", &RuntimeTreeEnsembleRegressorDouble::target_ids_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_readonly("target_weights_", &RuntimeTreeEnsembleRegressorDouble::target_weights_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_readonly("base_values_", &RuntimeTreeEnsembleRegressorDouble::base_values_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_readonly("n_targets_", &RuntimeTreeEnsembleRegressorDouble::n_targets_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    cld.def_readonly("post_transform_", &RuntimeTreeEnsembleRegressorDouble::post_transform_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    // cld.def_readonly("leafnode_data_", &RuntimeTreeEnsembleRegressorDouble::leafnode_data_, "See :ref:`lpyort-TreeEnsembleRegressorDouble`.");
    
    cld.def("debug_threshold", &RuntimeTreeEnsembleRegressorDouble::debug_threshold,
        "Checks every features against every features against every threshold. Returns a matrix of boolean.");
    cld.def("compute_tree_outputs", &RuntimeTreeEnsembleRegressorDouble::compute_tree_outputs,
        "Computes every tree output.");
    cld.def_readonly("same_mode_", &RuntimeTreeEnsembleRegressorDouble::same_mode_, "Tells if all nodes applies the same rule for thresholds.");
    cld.def_readonly("consecutive_leaf_data_", &RuntimeTreeEnsembleRegressorDouble::consecutive_leaf_data_,
        "Tells if there are two consecutive targets sharing the same node and the same tree (it should not happen in 1D target).");
}

#endif
