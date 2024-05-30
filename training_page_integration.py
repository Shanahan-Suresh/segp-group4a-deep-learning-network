from torchvision.utils import save_image
import setup

def get_image(produced_image, original_image):
    save_produced_image_tensor(produced_image)
    save_original_image_tensor(original_image)

# Save tensor from produced image
def save_produced_image_tensor(image_tensor):
    image_tensor = image_tensor.squeeze(0)
    image_tensor = image_tensor.swapaxes(2, 1)
    image_tensor = image_tensor.swapaxes(1, 0)
    save_image(image_tensor, "Temp files/train_image.png")

# Save tensor from original image
def save_original_image_tensor(image_tensor):
    image_tensor = image_tensor.squeeze(0)
    image_tensor = image_tensor.swapaxes(2, 1)
    image_tensor = image_tensor.swapaxes(1, 0)
    save_image(image_tensor, "Temp files/original_image.png")

# Change display image based on saved image
def refresh_image(preview_image, original_image_widget):
    preview_image.setStyleSheet(setup.TrainingGeneratedImage)
    original_image_widget.setStyleSheet(setup.TrainingOriginalImage)

# Progress bar update
def update_progress_bar(progress_bar, progress, epoch_num):
    progress_bar.setValue(int((progress / epoch_num) * 100))

# Loss bar update
def update_loss_bar(epoch_loss, total_loss, epoch_loss_widget, total_loss_widget):
    epoch_loss = epoch_loss.cpu().detach().numpy()
    epoch_loss_widget.setText("Epoch Loss : " + str(epoch_loss)[0:6])
    total_loss_widget.setText("Training Loss : " + str(total_loss.item())[0:6])
