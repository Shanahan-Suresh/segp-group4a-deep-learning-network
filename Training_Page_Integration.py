from torchvision.utils import save_image

def get_image(produced_image,original_image):
    save_produced_image_tensor(produced_image)
    save_original_image_tensor(original_image)

def save_produced_image_tensor(image_tensor):
    image_tensor = image_tensor.squeeze(0)
    image_tensor = image_tensor.swapaxes(2, 1)
    image_tensor = image_tensor.swapaxes(1, 0)

    save_image(image_tensor,"train_image.png")
def save_original_image_tensor(image_tensor):
    image_tensor = image_tensor.squeeze(0)
    image_tensor = image_tensor.swapaxes(2, 1)
    image_tensor = image_tensor.swapaxes(1, 0)
    save_image(image_tensor,"original_image.png")
def refresh_image(preview_image,original_image_widget):
    preview_image.setStyleSheet("image: url(train_image.png);border :1px solid black;")
    original_image_widget.setStyleSheet("image: url(original_image.png);border :1px solid black;")


def update_progress_bar(progress_bar,epoch,epoch_num):
    progress_bar.setValue(((epoch+1)/epoch_num)*100)
def update_loss_bar(epoch_loss,total_loss, epoch_loss_widget, total_loss_widget):
    epoch_loss = epoch_loss.detach().numpy()
    epoch_loss_widget.setText("Epoch Loss : " + str(epoch_loss))
    total_loss_widget.setText("Training Loss : " + str(total_loss.item()))
