from keras.models import Sequential #for creating models layer-by-layer
from keras.layers import Dense
from keras.utils.vis_utils import plot_model
from sklearn.datasets import make_moons
from matplotlib import pyplot
from keras.callbacks import ModelCheckpoint
from keras.models import load_model
from keras.callbacks import EarlyStopping

#model with one input variable, a hidden layer with two neurons, and an output layer with one binary output

model = Sequential()
model.add(Dense(2, input_dim=1, activation='relu')) #no. of nodes, specify input dim at the first layer, specify activaction function
model.add(Dense(1, activation='sigmoid'))
print(model.summary())

# plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
#params= (input*neurons)+bias

X, y = make_moons(n_samples=100, noise=0.2, random_state=1)
for i in range(len(y)):
  if y[i]==0:
    pyplot.plot(X[:, 0][i],X[:, 1][i],'o',c='r')
  else:
    pyplot.plot(X[:, 0][i],X[:, 1][i],'o',c='b')
pyplot.show()

# split into train and test
n_train = 30
trainX, testX = X[:n_train, :], X[n_train:, :]
trainy, testy = y[:n_train], y[n_train:]

for i in range(len(trainy)):
  if trainy[i]==0:
    pyplot.plot(trainX[:, 0][i],trainX[:, 1][i],'o',c='r')
  else:
    pyplot.plot(trainX[:, 0][i],trainX[:, 1][i],'o',c='b')
pyplot.show()

for i in range(len(testy)):
  if testy[i]==0:
    pyplot.plot(testX[:, 0][i],testX[:, 1][i],'o',c='yellow')
  else:
    pyplot.plot(testX[:, 0][i],testX[:, 1][i],'o',c='pink')
pyplot.show()

# define model
model = Sequential()
model.add(Dense(500, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) #specifying a loss (distance between the current output and the expected output), metrics (monitor and measure the performance of a model), and an optimizer (modifies the attributes of the neural network, such as weights and learning rate)
print(model.summary())

# simple early stopping
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1)

# fit model
history = model.fit(trainX, trainy, validation_data=(testX, testy), epochs=4000, verbose=0, callbacks=[es])
# evaluate the model
_, train_acc = model.evaluate(trainX, trainy, verbose=0)
_, test_acc = model.evaluate(testX, testy, verbose=0)
print('Train: %.3f, Test: %.3f' % (train_acc, test_acc))
# plot training history
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='valid')
pyplot.legend()
pyplot.show()




