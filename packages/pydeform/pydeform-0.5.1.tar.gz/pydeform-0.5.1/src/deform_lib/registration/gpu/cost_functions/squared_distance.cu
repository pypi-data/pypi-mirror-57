#include "cost_function_kernel.h"
#include "squared_distance.h"

namespace cuda {
    using namespace stk::cuda;
}

template<typename T>
struct SSDImpl
{
    typedef T VoxelType;

    SSDImpl() {}

    __device__ float operator()(
        const cuda::VolumePtr<VoxelType>& fixed,
        const cuda::VolumePtr<VoxelType>& moving,
        const dim3& fixed_dims,
        const dim3& moving_dims,
        const int3& fixed_p,
        const float3& moving_p,
        const float3& /*d*/
    )
    {
        auto const lab = cuda::linear_at_border<float>;
        const T val_fixed = fixed(fixed_p.x, fixed_p.y, fixed_p.z);
        const T val_moving = lab(moving, moving_dims, moving_p.x, moving_p.y, moving_p.z);
        const T diff = val_fixed - val_moving;
        return diff * diff;
    }
};

void GpuCostFunction_SSD::cost(
    GpuDisplacementField& df,
    const float3& delta,
    float weight,
    const int3& offset,
    const int3& dims,
    Settings::UpdateRule update_rule,
    stk::GpuVolume& cost_acc,
    stk::cuda::Stream& stream
)
{
    ASSERT(cost_acc.voxel_type() == stk::Type_Float2);

    FATAL_IF(_fixed.voxel_type() != stk::Type_Float ||
             _moving.voxel_type() != stk::Type_Float ||
             _fixed_mask.valid() && _fixed_mask.voxel_type() != stk::Type_Float ||
             _moving_mask.valid() && _moving_mask.voxel_type() != stk::Type_Float)
        << "Unsupported pixel type";

    auto kernel = CostFunctionKernel<SSDImpl<float>>(
        SSDImpl<float>(),
        _fixed,
        _moving,
        _fixed_mask,
        _moving_mask,
        weight,
        cost_acc
    );

    invoke_cost_function_kernel(
        kernel,
        delta,
        offset,
        dims,
        df,
        update_rule,
        stream
    );
}

