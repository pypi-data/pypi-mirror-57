#!/usr/bin/env python
# ******************************************************************************
# Copyright 2019 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************

from tensorflow.keras import Model
from tensorflow.keras.layers import Input, Reshape, Activation

from ...quantization_blocks import conv_block, separable_conv_block

def mobilenet_kws(input_shape,
                  classes,
                  weights_quantization=0,
                  activ_quantization=0,
                  input_weights_quantization=None):

    img_input = Input(shape=input_shape)

    # Overrides input weights quantization if None
    if input_weights_quantization is None:
        input_weights_quantization = weights_quantization

    x = conv_block(img_input, filters=32, kernel_size=(5,5),
            padding='same',
            strides=(2, 2),
            use_bias=False,
            name='conv_0',
            weight_quantization=input_weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters = 64,
            kernel_size=(3,3),
            padding='same',
            use_bias=False,
            name='separable_1',
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters = 64,
            kernel_size=(3,3),
            padding='same',
            use_bias=False,
            name='separable_2',
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters = 64,
            kernel_size=(3,3),
            padding='same',
            use_bias=False,
            name='separable_3',
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters = 64,
            kernel_size=(3,3),
            padding='same',
            use_bias=False,
            name='separable_4',
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters = 64,
            kernel_size=(3,3),
            padding='same',
            use_bias=False,
            name='separable_5',
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            pooling='global_avg',
            add_batchnorm=True)

    shape = (1, 1, int(64))

    x = Reshape(shape, name='reshape_1')(x)

    x = separable_conv_block(x,
            filters = classes,
            kernel_size=(3,3),
            padding='same',
            use_bias=False,
            name='separable_6',
            weight_quantization=weights_quantization,
            activ_quantization=None)

    x = Activation('softmax', name='act_softmax')(x)

    x = Reshape((classes,), name='reshape_2')(x)

    model = Model(img_input, x, name='mobilenet_kws')

    return model
