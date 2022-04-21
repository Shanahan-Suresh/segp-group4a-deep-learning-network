from torchvision.utils import save_image

# link tensor from training page to model
import setup


def get_image(produced_image, original_image):
    save_produced_image_tensor(produced_image)
    save_original_image_tensor(original_image)


# save tensor from produced image
def save_produced_image_tensor(image_tensor):
    image_tensor = image_tensor.squeeze(0)
    image_tensor = image_tensor.swapaxes(2, 1)
    image_tensor = image_tensor.swapaxes(1, 0)
    save_image(image_tensor, "Temp files/train_image.png")


# save tensor from original image
def save_original_image_tensor(image_tensor):
    image_tensor = image_tensor.squeeze(0)
    image_tensor = image_tensor.swapaxes(2, 1)
    image_tensor = image_tensor.swapaxes(1, 0)
    save_image(image_tensor, "Temp files/original_image.png")


# change disaplay image based on saved image
def refresh_image(preview_image, original_image_widget):
    preview_image.setStyleSheet(setup.TrainingGeneratedImage)
    original_image_widget.setStyleSheet(setup.TrainingOriginalImage)


# progress bar update
def update_progress_bar(progress_bar, epoch, epoch_num):
    progress_bar.setValue(((epoch + 1) / epoch_num) * 100)


# loss bar update
def update_loss_bar(epoch_loss, total_loss, epoch_loss_widget, total_loss_widget):
    epoch_loss = epoch_loss.cpu().detach().numpy()
    epoch_loss_widget.setText("Epoch Loss : " + str(epoch_loss)[0:6])
    total_loss_widget.setText("Training Loss : " + str(total_loss.item())[0:6])
