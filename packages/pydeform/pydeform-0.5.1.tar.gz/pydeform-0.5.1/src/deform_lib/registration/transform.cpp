#include "displacement_field.h"
#include "transform.h"

#include <stk/common/log.h>
#include <stk/math/float3.h>

namespace
{
    template<typename TVoxelType>
    stk::VolumeHelper<TVoxelType> transform_volume_nn(
        const stk::VolumeHelper<TVoxelType>& src,
        const DisplacementField& df)
    {
        // Transformed volume will have the same dimensions and properties (origin and spacing)
        //  as the deformation field and not the source image. The deformation field is inherited
        //  from the fixed volume in the registration and we want to transform the moving image (src)
        //  to the fixed image space.

        // There should be no requirements on src to have the same size, spacing and origin as
        //  the fixed image.

        dim3 dims = df.size();

        stk::VolumeHelper<TVoxelType> out(dims);
        out.copy_meta_from(df.volume());

        #define FAST_ROUND(x_) int(x_+0.5f)

        #pragma omp parallel for
        for (int z = 0; z < int(dims.z); ++z) {
        for (int y = 0; y < int(dims.y); ++y) {
        for (int x = 0; x < int(dims.x); ++x) {
            const float3 moving_p = src.point2index(df.transform_index(int3{x,y,z}));

            out(x, y, z) = src.at(
                int(FAST_ROUND(moving_p.x)),
                int(FAST_ROUND(moving_p.y)),
                int(FAST_ROUND(moving_p.z)),
                stk::Border_Constant
            );
        }
        }
        }
        #undef FAST_ROUND

        return out;
    }

    template<typename TVoxelType>
    stk::VolumeHelper<TVoxelType> transform_volume_linear(
        const stk::VolumeHelper<TVoxelType>& src,
        const DisplacementField& df)
    {
        // Transformed volume will have the same dimensions and properties (origin and spacing)
        //  as the deformation field and not the source image. The deformation field is inherited
        //  from the fixed volume in the registration and we want to transform the moving image (src)
        //  to the fixed image space.

        // There should be no requirements on src to have the same size, spacing, origin, and direction
        //  as the fixed image.

        dim3 dims = df.size();

        stk::VolumeHelper<TVoxelType> out(dims);
        out.copy_meta_from(df.volume());

        #pragma omp parallel for
        for (int z = 0; z < int(dims.z); ++z) {
            for (int y = 0; y < int(dims.y); ++y) {
                for (int x = 0; x < int(dims.x); ++x) {
                    const float3 pt = df.transform_index(int3{x,y,z});
                    out(x, y, z) = src.linear_at_point(pt, stk::Border_Constant);
                }
            }
        }
        return out;
    }
}

stk::Volume transform_volume(const stk::Volume& src, const DisplacementField& df, transform::Interp interp)
{
    if (interp == transform::Interp_NN) {
        if (src.voxel_type() == stk::Type_Float) {
            return transform_volume_nn<float>(src, df);
        }
        else if (src.voxel_type() == stk::Type_Double) {
            return transform_volume_nn<double>(src, df);
        }
        else if (src.voxel_type() == stk::Type_UChar) {
            return transform_volume_nn<uint8_t>(src, df);
        }
        else {
            LOG(Error) << "transform_volume: Unsupported volume type (type: " << src.voxel_type() << ")";
        }
    }
    else if (interp == transform::Interp_Linear) {
        if (src.voxel_type() == stk::Type_Float) {
            return transform_volume_linear<float>(src, df);
        }
        else if (src.voxel_type() == stk::Type_Double) {
            return transform_volume_linear<double>(src, df);
        }
        else {
            LOG(Error) << "transform_volume: Unsupported volume type (type: " << src.voxel_type() << ")";
        }
    }
    else {
        LOG(Error) << "transform_volume: Unsupported interpolation method (given: " << interp << ")";
    }
    return stk::Volume();
}

stk::Volume transform_volume(const stk::Volume& src, const stk::VolumeFloat3& df, transform::Interp interp)
{
    return transform_volume(src, DisplacementField(df), interp);
}
