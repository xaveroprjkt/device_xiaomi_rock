#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    'system_ext/lib64/libsink.so': blob_fixup()
        .add_needed('libshim_sink.so'),
    'system_ext/lib64/libsource.so': blob_fixup()
        .add_needed('libui_shim.so'),
    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so'),
	.replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so'),
    ('vendor/bin/mtk_agpsd': blob_fixup()
	.replace_needed('libcrypto.so', 'libcrypto-v33.so'),
    ('vendor/bin/hw/android.hardware.gnss-service.mediatek', 'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),
    'vendor/bin/hw/vendor.mediatek.hardware.mtkpower@1.0-service': blob_fixup()
        .replace_needed('android.hardware.power-V2-ndk_platform.so', 'android.hardware.power-V2-ndk.so'),
    'vendor/bin/hw/android.hardware.vibrator-service.mediatek': blob_fixup()
	.replace_needed('android.hardware.vibrator-V2-ndk_platform.so', 'android.hardware.vibrator-V2-ndk.so'),
    'vendor/bin/hw/android.hardware.lights-service.mediatek': blob_fixup()
	.replace_needed('android.hardware.light-V1-ndk_platform.so', 'android.hardware.light-V1-ndk_platform.so'),
    ('vendor/etc/init/android.hardware.media.c2@1.2-mediatek.rc': blob_fixup()
	.regex_replace('@1.2-mediatek', '@1.2-mediatek-64b'),
    ('vendor/etc/init/android.hardware.graphics.allocator@4.0-service-mediatek.rc': blob_fixup()
	.regex_replace('android.hardware.graphics.allocator@4.0-service-mediatek', 'mt6789/android.hardware.graphics.allocator@4.0-service-mediatek.mt6789'),
    ('vendor/etc/init/android.hardware.bluetooth@1.1-service-mediatek.rc': blob_fixup()
	.regel_replace('on property:vts(.|\n)*', ''),
    'vendor/lib64/libvendor.goodix.hardware.biometrics.fingerprint@2.1.so': blob_fixup()
	.replace_needed('libhidltransport.so', 'libhidlbase-v32.so'),
    ('vendor/bin/mnld', 'vendor/lib64/mt6789/libaalservice.so', 'vendor/lib64/mt6789/libcam.utils.sensorprovider.so'): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),
    ('vendor/lib64/hw/mt6789/vendor.mediatek.hardware.pq@2.15-impl.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so')
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),
    ('vendor/lib64/mt6789/libmtkcam_stdutils.so', 'vendor/lib64/hw/mt6789/android.hardware.camera.provider@2.6-impl-mediatek.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so')
}  # fmt: skip

module = ExtractUtilsModule(
    'rock',
    'xiaomi',
    blob_fixups=blob_fixups,
    check_elf=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
