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

from tensorflow.keras.layers import Input
from tensorflow.keras import Model

from ...quantization_blocks import conv_block, separable_conv_block

def mobilenet_cifar10(input_shape,
                      classes=10,
                      weights_quantization=0,
                      activ_quantization=0,
                      input_weights_quantization=None):

    img_input = Input(shape=input_shape)

    # Overrides input weights quantization if None
    if input_weights_quantization is None:
        input_weights_quantization = weights_quantization

    x = conv_block(img_input, filters=128, name='conv_0',
            kernel_size=(3, 3),
            padding='same',
            use_bias=False,
            weight_quantization=input_weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=128, kernel_size=(3,3), name='separable_1',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=256, kernel_size=(3,3), name='separable_2',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=256, kernel_size=(3,3), name='separable_3',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            pooling='max',
            add_batchnorm=True)

    x = separable_conv_block(x, filters=512, kernel_size=(3,3), name='separable_4',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=512, kernel_size=(3,3), name='separable_5',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            pooling='max',
            add_batchnorm=True)

    x = separable_conv_block(x, filters=512, kernel_size=(3,3), name='separable_6',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=512, kernel_size=(3,3), name='separable_7',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            pooling='max',
            add_batchnorm=True)

    x = separable_conv_block(x, filters=1024, kernel_size=(3,3), name='separable_8',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=1024, kernel_size=(3,3), name='separable_9',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=activ_quantization,
            add_batchnorm=True)

    x = separable_conv_block(x, filters=classes, kernel_size=(3,3),
            name='separable_10',
            padding='same',
            use_bias=False,
            weight_quantization=weights_quantization,
            activ_quantization=None,
            pooling='global_avg',
            add_batchnorm=False)

    model = Model(img_input, x, name='mobilenet_cifar10')

    return model
