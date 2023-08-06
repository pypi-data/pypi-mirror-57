import matplotlib.pyplot as _plt

def learning_curves(history, rect = (0,0,1,1)):
    """
    plot learning curves for each metric
    """
    metrics = [key for key in history.history.keys() if key != 'lr' and 'val' not in key]

    fig, ax_list = _plt.subplots(1,len(metrics))
    
    if len(metrics)==1:
        ax_list = [ax_list]
    
    p=0
    for metric in metrics:
        for train_val_label in ['','val_']:
            label = train_val_label+metric
            ax_list[p].plot(history.epoch, history.history[label], label = label)
        ax_list[p].set_xlabel('epoch')
        ax_list[p].set_ylabel(metric)
        ax_list[p].legend()
        p+=1
    fig.tight_layout(rect=rect)
    _plt.show()