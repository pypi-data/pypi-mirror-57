/***************************************************************************
* Additional implementation of "BIKE: Bit Flipping Key Encapsulation". 
* Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
*
* Written by Nir Drucker and Shay Gueron
* AWS Cryptographic Algorithms Group
* (ndrucker@amazon.com, gueron@amazon.com)
*
* The license is detailed in the file LICENSE.md, and applies to this file.
* ***************************************************************************/

#pragma once

#include "aes.h"

//////////////////////////////
//        Types
/////////////////////////////

typedef struct aes_ctr_prf_state_s {
        uint128_t ctr;
        uint128_t buffer;
        aes256_ks_t ks;
        uint32_t rem_invokations;
        uint8_t pos;
} aes_ctr_prf_state_t;

//////////////////////////////
//        Methods
/////////////////////////////

ret_t init_aes_ctr_prf_state(OUT aes_ctr_prf_state_t *s,
                             IN  const uint32_t max_invokations,
                             IN  const seed_t *seed);

ret_t aes_ctr_prf(OUT uint8_t *a,
                  IN OUT aes_ctr_prf_state_t *s,
                  IN const uint32_t len);

_INLINE_ void finalize_aes_ctr_prf(IN OUT aes_ctr_prf_state_t *s)
{
    aes256_free_ks(&s->ks);
    secure_clean((uint8_t *)s, sizeof(*s));
}

_INLINE_ void aes_ctr_prf_state_cleanup(IN OUT aes_ctr_prf_state_t *s) 
{
    finalize_aes_ctr_prf(s);
}
