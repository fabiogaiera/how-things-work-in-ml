[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# How things work under the hood in Machine Learning

## Section 1 - Dataset Creation

Nowadays (and fortunately) we have TensorFlow among the most popular libraries for Machine Learning, which comes with many utilities out of the box, but have you ever wondered how you could implement your own functions in absence of TensorFlow or any other ML library?
<br/>
<br/>
Certailny I do not want to reinvent the wheel: ML libraries are developed by very talented engineers that collaborate accross the world, source code is available for everyone, they have become "de facto standards" and many other aspects that motivate us to use ML libraries, instead of creating our own libraries.
<br/>
<br/>
Just for understanding what happens under the hood when using a function in my code, I wondered how I could implement this API call from TensorFlow: <b>tf.keras.utils.image_dataset_from_directory</b> 
<br/>
<br/>
TensorFlow documentation simply says: Generates a tf.data.Dataset from image files in a directory.
<br/>
<br/>
Based on this, then my question was: Given a dataset composed by images, how can I convert it in a CSV file, where each row (sample) represents the input values (X), followed by the output value (y)?
<br/>
<br/>
The output dataset would be as follows: 
<br/>
<br/>

```

x11, x12, ..., x1n, y1 (Example 1)
x21, x22, ..., x2n, y2 (Example 2)
...
xn1, xn2, ..., xnn, yn (Example n)

```
<br/>
<br/>
I came accross with a simple solution using Python, NumPy and Pillow. For details, check the directory /notebooks/Dataset Creation.ipynb
<br/>
<br/>

## Section 2 - Model Creation, Model Training and Prediction

Given the dataset created in the previous section, let's build a machine learning model that can be used to predict on new samples (Horses or Humans)
<br/>
<br/>
The algorithm for building a machine learning model includes several steps, as follows:

```
- Initialize parameters

- Repeat

    - Forward propagation
    
    - Compute cost
    
    - Backward propagation
    
    - Update parameters (weights and biases)

  Until it reaches total of epochs 
```

Notice that implement the above steps in complex models can be a nightmare using only Python and NumPy. That's why we use a friendly ML library.

<br/>
What we usually do in TensorFlow:
<br/>
<br/>

1. We create a function that returns the *model architecture*.

```
def create_model(input_features):
    
    # Create an instance of Sequential class
    model = Sequential()
    
    # Add layers
    model.add(Dense(10, input_dim = input_features, activation = 'tanh')) 
    model.add(Dense(1, activation='sigmoid'))
    
    # Compile the model
    model.compile(loss='binary_crossentropy', optimizer='SGD', metrics=['accuracy'])
    
    return model
```

2. We train the model using the training dataset (Process in which the model *learns* the parameters such as weights and biases)

```
model.fit(X_training, y_training, epochs = 2000, verbose = 0)
```

3. Given a validation dataset, we evaluate the loss and accuracy of the model.

```
model.evaluate(X_validation, y_validation)
```

4. We use the model for predicting on new samples.

```
model.predict(some_new_sample)

```
For details, check the directory /notebooks/Model Creation, Model Training and Prediction.ipynb
