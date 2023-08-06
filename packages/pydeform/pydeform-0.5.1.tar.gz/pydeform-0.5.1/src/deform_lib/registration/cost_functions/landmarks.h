#pragma once

#include "sub_function.h"


struct LandmarksFunction : public SubFunction
{
    LandmarksFunction(const std::vector<float3>& fixed_landmarks,
                      const std::vector<float3>& moving_landmarks,
                      const stk::Volume& fixed,
                      const float decay) :
        _landmarks {fixed_landmarks},
        _fixed {fixed},
        _half_decay {decay / 2.0f}
    {
        ASSERT(fixed_landmarks.size() == moving_landmarks.size());
        for (size_t i = 0; i < fixed_landmarks.size(); ++i) {
            _displacements.push_back(moving_landmarks[i] - fixed_landmarks[i]);
        }
    }

    virtual ~LandmarksFunction() {}

    float cost(const int3& p, const float3& def)
    {
        float cost = 0.0f;
        const float epsilon = 1e-6f;

        const float3 world_p = _fixed.index2point(p);

        for (size_t i = 0; i < _landmarks.size(); ++i) {
            cost += stk::norm2(def - _displacements[i]) /
                    (std::pow(stk::norm2(_landmarks[i] - world_p), _half_decay) + epsilon);
        }

        return cost;
    }

    const std::vector<float3> _landmarks;
    std::vector<float3> _displacements;
    const stk::Volume _fixed;
    const float _half_decay;
};

