/*
 * Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */

#pragma once

#include "crypto/s2n_ecc.h"
#include "tls/s2n_connection.h"
#include "stuffer/s2n_stuffer.h"

#define S2N_SIZE_OF_EXTENSION_TYPE          2
#define S2N_SIZE_OF_EXTENSION_DATA_SIZE     2
#define S2N_SIZE_OF_CLIENT_SHARES_SIZE      2
#define S2N_SIZE_OF_NAMED_GROUP             2
#define S2N_SIZE_OF_KEY_SHARE_SIZE          2

extern int s2n_ecdhe_parameters_send(struct s2n_ecc_params *ecc_params, struct s2n_stuffer *out);
