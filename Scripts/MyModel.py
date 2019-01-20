from keras import models
from keras import layers

def RunModel(fea_t,lab_t,fea_v,lab_v):
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu',
                           input_shape=(37,)))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    history = model.fit(fea_t,
                        lab_t,
                        epochs=500,
                        batch_size=512,
                        validation_data=(fea_v, lab_v))
    return history