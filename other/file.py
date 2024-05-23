# Save the model to a file
model.save('my_model.h5')

parameters = {
   'epochs': epochs,
   'step_size_train': step_size_train,
   'class_indices': train_generator.class_indices
  
}
