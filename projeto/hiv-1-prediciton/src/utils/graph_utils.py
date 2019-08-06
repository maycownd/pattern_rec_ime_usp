import matplotlib.pyplot as plt


def plot_history(history):
    f, ax = plt.subplots(1, 2, figsize=(16, 7))

    acc = history.history['auc']
    val_acc = history.history['val_auc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(1, len(acc) + 1)

    plt.sca(ax[0])
    plt.plot(epochs, acc, 'bo', label='Training auc')
    plt.plot(epochs, val_acc, 'b', label='Validation auc')
    plt.title('Training and validation auc')
    plt.legend()

    plt.sca(ax[1])
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()

    plt.show()
