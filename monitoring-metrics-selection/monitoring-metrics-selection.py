import numpy as np
def compute_monitoring_metrics(system_type, y_true, y_pred):
    """
    Compute the appropriate monitoring metrics for the given system type.
    """
    # Write code here
    tp = sum(t == 1 and p == 1 for t, p in zip(y_true, y_pred))
    tn = sum(t == 0 and p == 0 for t, p in zip(y_true, y_pred))
    fp = sum(t == 0 and p == 1 for t, p in zip(y_true, y_pred))
    fn = sum(t == 1 and p == 0 for t, p in zip(y_true, y_pred))
    n = len(y_true)
    if system_type == 'classification':
        
        accuracy = (tp + tn) / n 
        precision = tp / (tp+fp) if (tp + fp) > 0 else 0
        recall = tp / (tp+fn) if (tp + fn) > 0 else 0
        f1 = 2*precision*recall / (precision + recall) if (precision + recall) > 0 else 0
        return [
                    ("accuracy", accuracy),
                    ("f1", f1),
                    ("precision", precision),
                    ("recall", recall),
                ]
    elif system_type == 'regression':
        y_abs_diff = np.abs(np.array(y_pred) - np.array(y_true))
        mae = np.mean(y_abs_diff)
        rmse = np.sqrt(np.mean(y_abs_diff**2))
        return [
                    ("mae", mae),
                    ("rmse", rmse)
                ]
    elif system_type == 'ranking':
        top_k_indices = sorted(range(len(y_pred)), key=lambda i: y_pred[i], reverse=True)[:3]
        
        relevant_in_top_k = sum(y_true[i] for i in top_k_indices)
        total_relevant = sum(y_true)
        
        precision_at_k = relevant_in_top_k / 3
        recall_at_k = relevant_in_top_k / total_relevant if total_relevant > 0 else 0.0
        
        return [
            ("precision_at_3", precision_at_k),
            ("recall_at_3", recall_at_k)
        ]
                
                
    
    pass