#!/bin/bash 

export IOS_VERSION="5.1"

function set_dev_env(){
    export XCODE_DEVROOT=`xcode-select -print-path`
    export PLATFORM_DEVROOT="${XCODE_DEVROOT}/Platforms/${PLATFORM}.platform/Developer"
    export SDKROOT="${PLATFORM_DEVROOT}/SDKs/${PLATFORM}${IOS_VERSION}.sdk"
    export ODIR="/Users/aco/devel/ios/dist/${PLATFORM}"
    export PATH=${PLATFORM_DEVROOT}/usr/bin:${ODIR}/bin:${PATH}
    export LDFLAGS="-Wl,-syslibroot,$SDKROOT ${ARCHFLAGS} -L${ODIR}/lib -Lextralibs"
    export OPTFLAGS="-pipe -O3 -I${ODIR}/include"
    export CFLAGS="-isysroot ${SDKROOT} ${PLATFORM_VERSION_MIN} ${ARCHFLAGS} ${OPTFLAGS}"
    export CXXFLAGS=${CFLAGS}
    export OBJCFLAGS=${CFLAGS}
    export OBJCXXFLAGS=${CFLAGS}
    export CC="clang"
    export CXX="clang++"
}

if [ "$1" == "sim" ]; then
    echo "Seting up environment for iPhoneSimulator"
    export PLATFORM="iPhoneSimulator"
    export MACOSX_DEPLOYMENT_TARGET="10.6"
    export PLATFORM_VERSION_MIN="-mmacosx-version-min=${MACOSX_DEPLOYMENT_TARGET}"
    export ARCHFLAGS="-arch i386 -m32"
    set_dev_env
elif [ "$1" == "dev" ]; then
    echo "Seting up environment for iPhoneOS"
    export PLATFORM="iPhoneOS"
    export IPHONEOS_DEPLOYMENT_TARGET="${IOS_VERSION}"
    export PLATFORM_VERSION_MIN="-miphoneos-version-min=${IPHONEOS_DEPLOYMENT_TARGET}"
    export ARCHFLAGS="-arch armv7 -m32 -mcpu=cortex-a8 -mno-thumb -mfpu=neon -mfloat-abi=softfp"
    # -ftree-vectorize -ffast-math -fsingle-precision-constant
    set_dev_env
else
    echo "What now?"
    echo "Usage: source env.sh [sim|dev]"
    echo "       dev for iPhoneOS"
    echo "       sim for iPhoneSimulator"
    exit 1
fi
export PS1="[${PLATFORM}] \w> "

