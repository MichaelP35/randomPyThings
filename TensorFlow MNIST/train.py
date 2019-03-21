# Sets Up TensorFlow Along With The MNIST Dataset. Three Training Sessions Are Also Conducted
import tensorflow as tf  # Google's Deep Learning Library

mnist = tf.keras.datasets.mnist  # Dataset Of 28x28 Images Of Handwritten Digits
(x_train, y_train), (x_test, y_test) = mnist.load_data()  # Unpacks Images to x_train/x_test and y_train/y_test

x_train = tf.keras.utils.normalize(x_train, axis=1)  # Scales Data Between 0 And 1
x_test = tf.keras.utils.normalize(x_test, axis=1)  # Scales Data Between 0 And 1

model = tf.keras.models.Sequential()  # Basic Feed-Forward Model
model.add(tf.keras.layers.Flatten())  # Resizes Images To 1x784
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # Simple Fully-Connected Layer: 128 units
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))  # Output Layer: 10 Units For 10 Classes

model.compile(optimizer='adam',  # Adam Optimizer (Great For Starters)
              loss='sparse_categorical_crossentropy',  # Calculate Loss
              metrics=['accuracy'])  # Track Accuracy

model.fit(x_train, y_train, epochs=3)  # 3 Training Sessions

val_loss, val_acc = model.evaluate(x_test, y_test)  # Evaluate Output
print(val_loss)  # Model's Loss
print(val_acc)  # Model's Accuracy

model.save('mnist-test.model')  # Saves The Model
