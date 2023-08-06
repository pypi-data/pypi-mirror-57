#include <deform_lib/arg_parser.h>
#include <deform_lib/config.h>
#include <deform_lib/defer.h>
#include <deform_lib/filters/resample.h>
#include <deform_lib/jacobian.h>
#include <deform_lib/make_unique.h>
#include <deform_lib/profiler/profiler.h>
#include <deform_lib/registration/landmarks.h>
#include <deform_lib/registration/registration.h>
#include <deform_lib/registration/registration_engine.h>
#include <deform_lib/registration/settings.h>
#include <deform_lib/registration/transform.h>
#include <deform_lib/registration/volume_pyramid.h>
#include <deform_lib/registration/voxel_constraints.h>

#include <stk/common/assert.h>
#include <stk/common/log.h>
#include <stk/filters/normalize.h>
#include <stk/image/volume.h>
#include <stk/io/io.h>

#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <omp.h>
#include <sstream>
#include <string>
#include <vector>

#include "deform/command.h"

// NOTE: signal handling is unsafe and may generate deadlocks. Caveat emptor.
#if defined(DF_SIGNAL_HANDLER) && defined(DF_USE_BACKWARD)
    #include "backward.hpp"
    namespace backward {
        backward::SignalHandling sh;
    } // namespace backward
#endif

namespace
{
    void print_command_help(const char* exec)
    {
        std::cout << "Usage: " << exec << " COMMAND ..." << std::endl << std::endl;
        std::cout << "COMMANDS:" << std::endl << std::endl;

        std::cout << std::string(4, ' ') << std::setw(30) << std::left << "registration"
                  << "Performs image registration" << std::endl;
        std::cout << std::string(4, ' ') << std::setw(30) << std::left << "transform"
                  << "Transforms a volume with a given displacement field" << std::endl;
        std::cout << std::string(4, ' ') << std::setw(30) << std::left << "regularize"
                  << "Regularizes a displacement field" << std::endl;
        std::cout << std::string(4, ' ') << std::setw(30) << std::left << "jacobian"
                  << "Computes the Jacobian determinants of a displacement field" << std::endl;
        std::cout << std::string(4, ' ') << std::setw(30) << std::left << "divergence"
                  << "Computes the divergence of a displacement field" << std::endl;
        std::cout << std::endl;
    }

} // namespace

void print_version()
{
    std::cout << deform::version_string() << std::endl;
}

int main(int argc, char* argv[])
{
    PROFILER_INIT();
    defer{PROFILER_SHUTDOWN();};

    for (int i = 1; i < argc; ++i) {
        if (std::strcmp(argv[i], "--version") == 0) {
            print_version();
            return EXIT_SUCCESS;
        }
    }

    std::unique_ptr<DeformCommand> command;
    if (argc >= 2 && std::strcmp(argv[1], "registration") == 0) {
        command = make_unique<RegistrationCommand>(argc, argv, true);
    }
    else if (argc >= 2 && std::strcmp(argv[1], "transform") == 0) {
        command = make_unique<TransformCommand>(argc, argv);
    }
    else if (argc >= 2 && std::strcmp(argv[1], "regularize") == 0) {
        command = make_unique<RegularisationCommand>(argc, argv);
    }
    else if (argc >= 2 && std::strcmp(argv[1], "jacobian") == 0) {
        command = make_unique<JacobianCommand>(argc, argv);
    }
    else if (argc >= 2 && std::strcmp(argv[1], "divergence") == 0) {
        command = make_unique<DivergenceCommand>(argc, argv);
    }
    else {
        print_command_help(argv[0]);
        return EXIT_FAILURE;
    }

    return command->execute();
}

