#!/usr/bin/env python
#
# test_add_disk.py - test cases for the COTAddDisk class
#
# January 2015, Glenn F. Matthews
# Copyright (c) 2013-2017 the COT project developers.
# See the COPYRIGHT.txt file at the top-level directory of this distribution
# and at https://github.com/glennmatthews/cot/blob/master/COPYRIGHT.txt.
#
# This file is part of the Common OVF Tool (COT) project.
# It is subject to the license terms in the LICENSE.txt file found in the
# top-level directory of this distribution and at
# https://github.com/glennmatthews/cot/blob/master/LICENSE.txt. No part
# of COT, including this file, may be copied, modified, propagated, or
# distributed except according to the terms contained in the LICENSE.txt file.

"""Unit test cases for the COT.add_disk.COTAddDisk class."""

import filecmp
import os.path
import re
import mock

from COT.commands.tests.command_testcase import CommandTestCase
from COT.commands.add_disk import COTAddDisk
from COT.data_validation import InvalidInputError, ValueMismatchError
from COT.data_validation import ValueUnsupportedError, ValueTooHighError
from COT.disks import DiskRepresentation
from COT.disks.qcow2 import QCOW2


# pylint: disable=missing-param-doc,missing-type-doc

class TestCOTAddDisk(CommandTestCase):
    """Test cases for the COTAddDisk module."""

    command_class = COTAddDisk

    def test_readiness(self):
        """Test ready_to_run() under various combinations of parameters."""
        self.command.package = self.input_ovf
        ready, reason = self.command.ready_to_run()
        self.assertFalse(ready)
        self.assertTrue(re.search("DISK_IMAGE is a mandatory", reason))
        self.assertRaises(InvalidInputError, self.command.run)

        self.command.disk_image = self.blank_vmdk
        ready, reason = self.command.ready_to_run()
        self.assertTrue(ready)

        self.command.address = "1:0"
        ready, reason = self.command.ready_to_run()
        self.assertFalse(ready)
        self.assertTrue(re.search("controller", reason))
        self.assertRaises(InvalidInputError, self.command.run)

        self.command.controller = "ide"
        ready, reason = self.command.ready_to_run()
        self.assertTrue(ready)

        # address without controller is not allowed,
        # but controller without address is OK
        self.command.address = None
        ready, reason = self.command.ready_to_run()
        self.assertTrue(ready)

    def test_conflicting_args_1(self):
        """Test conflicting arguments are detected and rejected."""
        # TODO - it would be nice to detect this in ready_to_run()
        # rather than run()
        self.command.package = self.input_ovf
        self.command.disk_image = self.blank_vmdk
        # file2 exists and is mapped to IDE 1:0 but we request IDE 1:1
        self.command.controller = "ide"
        self.command.address = "1:1"
        self.command.file_id = "file2"
        self.assertRaises(ValueMismatchError, self.command.run)
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)

    def test_conflicting_args_2(self):
        """Test conflicting arguments are detected and rejected."""
        # TODO - it would be nice to detect this in ready_to_run()
        # rather than run()
        self.command.package = self.input_ovf
        self.command.disk_image = self.input_iso
        # ovf contains input.iso but we're asking it to overwrite input.vmdk
        self.command.file_id = "vmdisk1"
        self.assertRaises(ValueMismatchError, self.command.run)
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_CDROM)

    def test_conflicting_args_3(self):
        """Test conflicting arguments are detected and rejected."""
        # TODO - it would be nice to detect this in ready_to_run()
        # rather than run()
        self.command.package = self.input_ovf
        self.command.disk_image = self.input_vmdk
        # ovf contains input.vmdk but we're asking it to overwrite input.iso
        self.command.controller = "ide"
        self.command.address = "1:0"
        self.assertRaises(ValueMismatchError, self.command.run)
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)

    def test_new_hard_disk(self):
        """Test adding a new hard disk to the OVF."""
        self.command.package = self.input_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.run()
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.assertLogged(**self.CONTROLLER_TYPE_GUESSED_IDE)
        self.command.finished()
        self.check_diff("""
     <ovf:File ovf:href="sample_cfg.txt" ovf:id="textfile" \
ovf:size="{cfg_size}" />
+    <ovf:File ovf:href="blank.vmdk" ovf:id="blank.vmdk" \
ovf:size="{blank_size}" />
   </ovf:References>
...
     <ovf:Disk ovf:capacity="1" ovf:capacityAllocationUnits="byte * 2^30" \
ovf:diskId="vmdisk1" ovf:fileRef="file1" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
+    <ovf:Disk ovf:capacity="512" ovf:capacityAllocationUnits="byte * 2^20" \
ovf:diskId="blank.vmdk" ovf:fileRef="blank.vmdk" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
   </ovf:DiskSection>
...
       </ovf:Item>
+      <ovf:Item>
+        <rasd:AddressOnParent>0</rasd:AddressOnParent>
+        <rasd:ElementName>Hard Disk Drive</rasd:ElementName>
+        <rasd:HostResource>ovf:/disk/blank.vmdk</rasd:HostResource>
+        <rasd:InstanceID>14</rasd:InstanceID>
+        <rasd:Parent>5</rasd:Parent>
+        <rasd:ResourceType>17</rasd:ResourceType>
+      </ovf:Item>
     </ovf:VirtualHardwareSection>
""".format(cfg_size=self.FILE_SIZE['sample_cfg.txt'],
           blank_size=self.FILE_SIZE['blank.vmdk']))
        # Make sure the disk file is copied over
        self.assertTrue(filecmp.cmp(self.blank_vmdk,
                                    os.path.join(self.temp_dir, "blank.vmdk")),
                        "disk file should be exported unchanged")

    def test_new_hard_disk_relative_path(self):
        """Test adding a new hard disk with relative path to the OVF."""
        os.chdir(os.path.dirname(self.blank_vmdk))
        self.command.package = os.path.relpath(self.input_ovf)
        self.command.disk_image = os.path.basename(self.blank_vmdk)
        self.command.run()
        # COT should fixup the relative path to absolute path, avoiding this:
        # self.assertLogged(**self.FILE_REF_RELATIVE)
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.assertLogged(**self.CONTROLLER_TYPE_GUESSED_IDE)
        self.command.finished()
        self.check_diff("""
     <ovf:File ovf:href="sample_cfg.txt" ovf:id="textfile" \
ovf:size="{cfg_size}" />
+    <ovf:File ovf:href="blank.vmdk" ovf:id="blank.vmdk" \
ovf:size="{blank_size}" />
   </ovf:References>
...
     <ovf:Disk ovf:capacity="1" ovf:capacityAllocationUnits="byte * 2^30" \
ovf:diskId="vmdisk1" ovf:fileRef="file1" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
+    <ovf:Disk ovf:capacity="512" ovf:capacityAllocationUnits="byte * 2^20" \
ovf:diskId="blank.vmdk" ovf:fileRef="blank.vmdk" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
   </ovf:DiskSection>
...
       </ovf:Item>
+      <ovf:Item>
+        <rasd:AddressOnParent>0</rasd:AddressOnParent>
+        <rasd:ElementName>Hard Disk Drive</rasd:ElementName>
+        <rasd:HostResource>ovf:/disk/blank.vmdk</rasd:HostResource>
+        <rasd:InstanceID>14</rasd:InstanceID>
+        <rasd:Parent>5</rasd:Parent>
+        <rasd:ResourceType>17</rasd:ResourceType>
+      </ovf:Item>
     </ovf:VirtualHardwareSection>
""".format(cfg_size=self.FILE_SIZE['sample_cfg.txt'],
           blank_size=self.FILE_SIZE['blank.vmdk']))
        # Make sure the disk file is copied over
        self.assertTrue(filecmp.cmp(self.blank_vmdk,
                                    os.path.join(self.temp_dir, "blank.vmdk")),
                        "disk file should be exported unchanged")

    def test_new_hard_disk_and_explicit_controller(self):
        """Test adding a hard disk to an explicitly new SCSI controller."""
        self.command.package = self.input_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.controller = "scsi"
        self.command.address = "1:0"
        self.command.run()
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.command.finished()
        self.check_diff("""
     <ovf:File ovf:href="sample_cfg.txt" ovf:id="textfile" \
ovf:size="{cfg_size}" />
+    <ovf:File ovf:href="blank.vmdk" ovf:id="blank.vmdk" \
ovf:size="{blank_size}" />
   </ovf:References>
...
     <ovf:Disk ovf:capacity="1" ovf:capacityAllocationUnits="byte * 2^30" \
ovf:diskId="vmdisk1" ovf:fileRef="file1" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
+    <ovf:Disk ovf:capacity="512" ovf:capacityAllocationUnits="byte * 2^20" \
ovf:diskId="blank.vmdk" ovf:fileRef="blank.vmdk" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
   </ovf:DiskSection>
...
       </ovf:Item>
+      <ovf:Item>
+        <rasd:Address>1</rasd:Address>
+        <rasd:Description>SCSI Controller 1</rasd:Description>
+        <rasd:ElementName>SCSI Controller</rasd:ElementName>
+        <rasd:InstanceID>14</rasd:InstanceID>
+        <rasd:ResourceSubType>lsilogic</rasd:ResourceSubType>
+        <rasd:ResourceType>6</rasd:ResourceType>
+      </ovf:Item>
+      <ovf:Item>
+        <rasd:AddressOnParent>0</rasd:AddressOnParent>
+        <rasd:ElementName>Hard Disk Drive</rasd:ElementName>
+        <rasd:HostResource>ovf:/disk/blank.vmdk</rasd:HostResource>
+        <rasd:InstanceID>15</rasd:InstanceID>
+        <rasd:Parent>14</rasd:Parent>
+        <rasd:ResourceType>17</rasd:ResourceType>
+      </ovf:Item>
     </ovf:VirtualHardwareSection>
""".format(cfg_size=self.FILE_SIZE['sample_cfg.txt'],
           blank_size=self.FILE_SIZE['blank.vmdk']))
        # Make sure the disk file is copied over
        self.assertTrue(filecmp.cmp(self.blank_vmdk,
                                    os.path.join(self.temp_dir, "blank.vmdk")),
                        "disk file should be exported unchanged")

    def test_new_hard_disk_and_automatic_controller(self):
        """Add a new hard disk and create an IDE controller automatically."""
        # Since the primary IDE0 controller is already full in the IOSv OVF,
        # COT will need to automatically create IDE1 controller
        self.command.package = self.iosv_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.run()
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.assertLogged(**self.CONTROLLER_TYPE_GUESSED_IDE)
        self.assertLogged(**self.ADDRESS_ON_PARENT_NOT_SPECIFIED)
        self.command.finished()
        self.check_diff(file1=self.iosv_ovf,
                        expected="""
     <ovf:File ovf:href="input.vmdk" ovf:id="vios-adventerprisek9-m.vmdk" \
ovf:size="{input_size}" />
+    <ovf:File ovf:href="blank.vmdk" ovf:id="blank.vmdk" \
ovf:size="{blank_size}" />
   </ovf:References>
...
     <ovf:Disk ovf:capacity="1073741824" ovf:capacityAllocationUnits="byte" \
ovf:diskId="vios-adventerprisek9-m.vmdk" \
ovf:fileRef="vios-adventerprisek9-m.vmdk" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
+    <ovf:Disk ovf:capacity="512" ovf:capacityAllocationUnits="byte * 2^20" \
ovf:diskId="blank.vmdk" ovf:fileRef="blank.vmdk" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
   </ovf:DiskSection>
...
       </ovf:Item>
+      <ovf:Item>
+        <rasd:Address>1</rasd:Address>
+        <rasd:Description>IDE Controller 1</rasd:Description>
+        <rasd:ElementName>IDE Controller</rasd:ElementName>
+        <rasd:InstanceID>6</rasd:InstanceID>
+        <rasd:ResourceSubType>virtio</rasd:ResourceSubType>
+        <rasd:ResourceType>5</rasd:ResourceType>
+      </ovf:Item>
+      <ovf:Item>
+        <rasd:AddressOnParent>0</rasd:AddressOnParent>
+        <rasd:ElementName>Hard Disk Drive</rasd:ElementName>
+        <rasd:HostResource>ovf:/disk/blank.vmdk</rasd:HostResource>
+        <rasd:InstanceID>7</rasd:InstanceID>
+        <rasd:Parent>6</rasd:Parent>
+        <rasd:ResourceType>17</rasd:ResourceType>
+      </ovf:Item>
       <ovf:Item ovf:required="false">"""
                        .format(input_size=self.FILE_SIZE['input.vmdk'],
                                blank_size=self.FILE_SIZE['blank.vmdk']))

    def test_new_hard_disk_v09(self):
        """Test adding a disk to a version 0.9 OVF."""
        self.command.package = self.v09_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.run()
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.assertLogged(**self.CONTROLLER_TYPE_GUESSED_IDE)
        self.command.finished()
        # Default controller for generic platform is IDE for hard disks
        self.check_diff(file1=self.v09_ovf,
                        expected="""
     <ovf:File ovf:href="input.vmdk" ovf:id="file1" ovf:size="{input_size}" />
+    <ovf:File ovf:href="blank.vmdk" ovf:id="blank.vmdk" \
ovf:size="{blank_size}" />
   </ovf:References>
...
     <ovf:Disk ovf:capacity="1073741824" ovf:diskId="vmdisk1" \
ovf:fileRef="file1" ovf:format="http://www.vmware.com/specifications/\
vmdk.html#sparse" />
+    <ovf:Disk ovf:capacity="536870912" ovf:diskId="blank.vmdk" \
ovf:fileRef="blank.vmdk" ovf:format="http://www.vmware.com/interfaces/\
specifications/vmdk.html#streamOptimized" />
   </ovf:Section>
...
       </ovf:Item>
+      <ovf:Item>
+        <rasd:Caption>Hard Disk Drive</rasd:Caption>
+        <rasd:InstanceId>9</rasd:InstanceId>
+        <rasd:ResourceType>17</rasd:ResourceType>
+        <rasd:HostResource>/disk/blank.vmdk</rasd:HostResource>
+        <rasd:Parent>5</rasd:Parent>
+        <rasd:AddressOnParent>1</rasd:AddressOnParent>
+      </ovf:Item>
     </ovf:Section>""".format(input_size=self.FILE_SIZE['input.vmdk'],
                              blank_size=self.FILE_SIZE['blank.vmdk']))

    def test_new_hard_disk_v20_vbox(self):
        """Test adding a new hard disk to a v2.0 OVF from VirtualBox."""
        self.command.package = self.v20_vbox_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.run()
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.assertLogged(**self.CONTROLLER_TYPE_GUESSED_IDE)
        self.command.finished()
        # TODO - vbox XML is not very clean so the diffs are large...
        # self.check_diff('', file1=self.v20_vbox_ovf)

        # ovftool does not consider vbox ovfs to be valid
        self.validate_output_with_ovftool = False

    def test_overwrite_hard_disk_fileid(self):
        """Overwrite an existing disk by specifying matching file-id."""
        self.command.package = self.input_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.file_id = 'file1'
        # For coverage's sake, let's change the controller subtype too
        self.command.subtype = "virtio"
        self.command.run()
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.assertLogged(**self.OVERWRITING_FILE)
        self.assertLogged(**self.OVERWRITING_DISK)
        self.assertLogged(**self.OVERWRITING_DISK_ITEM)
        self.command.finished()
        self.check_diff("""
   <ovf:References>
-    <ovf:File ovf:href="input.vmdk" ovf:id="file1" ovf:size="{input_size}" />
+    <ovf:File ovf:href="blank.vmdk" ovf:id="file1" ovf:size="{blank_size}" />
     <ovf:File ovf:href="input.iso" ovf:id="file2" ovf:size="{iso_size}" />
...
     <ovf:Info>Virtual disk information</ovf:Info>
-    <ovf:Disk ovf:capacity="1" ovf:capacityAllocationUnits="byte * 2^30" \
ovf:diskId="vmdisk1" ovf:fileRef="file1" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
+    <ovf:Disk ovf:capacity="512" ovf:capacityAllocationUnits="byte * 2^20" \
ovf:diskId="vmdisk1" ovf:fileRef="file1" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
   </ovf:DiskSection>
...
         <rasd:InstanceID>3</rasd:InstanceID>
-        <rasd:ResourceSubType>lsilogic</rasd:ResourceSubType>
+        <rasd:ResourceSubType>virtio</rasd:ResourceSubType>
         <rasd:ResourceType>6</rasd:ResourceType>
""".format(input_size=self.FILE_SIZE['input.vmdk'],
           blank_size=self.FILE_SIZE['blank.vmdk'],
           iso_size=self.FILE_SIZE['input.iso']))
        # Make sure the old disk is not copied
        self.assertFalse(os.path.exists(os.path.join(self.temp_dir,
                                                     "input.vmdk")),
                         "old disk should be replaced, not exported")
        # Make sure the new disk is copied
        self.assertTrue(filecmp.cmp(self.blank_vmdk,
                                    os.path.join(self.temp_dir, "blank.vmdk")),
                        "newly added disk should be exported unchanged")

    def test_overwrite_hard_disk_address(self):
        """Overwrite an existing disk by matching controller address."""
        self.command.package = self.input_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.controller = 'scsi'
        self.command.address = "0:0"
        self.command.run()
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.assertLogged(**self.OVERWRITING_FILE)
        self.assertLogged(**self.OVERWRITING_DISK)
        self.assertLogged(**self.OVERWRITING_DISK_ITEM)
        self.command.finished()
        self.check_diff("""
   <ovf:References>
-    <ovf:File ovf:href="input.vmdk" ovf:id="file1" ovf:size="{input_size}" />
+    <ovf:File ovf:href="blank.vmdk" ovf:id="file1" ovf:size="{blank_size}" />
     <ovf:File ovf:href="input.iso" ovf:id="file2" ovf:size="{iso_size}" />
...
     <ovf:Info>Virtual disk information</ovf:Info>
-    <ovf:Disk ovf:capacity="1" ovf:capacityAllocationUnits="byte * 2^30" \
ovf:diskId="vmdisk1" ovf:fileRef="file1" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
+    <ovf:Disk ovf:capacity="512" ovf:capacityAllocationUnits="byte * 2^20" \
ovf:diskId="vmdisk1" ovf:fileRef="file1" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
   </ovf:DiskSection>
""".format(input_size=self.FILE_SIZE['input.vmdk'],
           blank_size=self.FILE_SIZE['blank.vmdk'],
           iso_size=self.FILE_SIZE['input.iso']))
        # Make sure the old disk is not copied
        self.assertFalse(os.path.exists(os.path.join(self.temp_dir,
                                                     "input.vmdk")),
                         "old disk should be replaced, not exported")
        # Make sure the new disk is copied
        self.assertTrue(filecmp.cmp(self.blank_vmdk,
                                    os.path.join(self.temp_dir, "blank.vmdk")),
                        "new disk should be exported unchanged")

    def test_overwrite_harddisk_with_cdrom(self):
        """Replace a hard disk with a cd-rom."""
        self.command.package = self.v09_ovf
        self.command.disk_image = self.input_iso
        self.command.drive_type = 'cdrom'
        self.command.controller = 'scsi'
        self.command.address = "0:0"
        self.command.run()
        self.assertLogged(**self.OVERWRITING_FILE)
        self.assertLogged(**self.OVERWRITING_DISK)   # TODO can we block this?
        self.assertLogged(**self.OVERWRITING_DISK_ITEM)
        self.assertLogged(**self.DELETING_DISK)
        self.assertLogged(**self.DELETING_DISK_SECTION)
        self.command.finished()
        self.check_diff(file1=self.v09_ovf, expected="""
   <ovf:References>
-    <ovf:File ovf:href="input.vmdk" ovf:id="file1" ovf:size="{vmdk_size}" />
+    <ovf:File ovf:href="input.iso" ovf:id="file1" ovf:size="{iso_size}" />
   </ovf:References>
-  <ovf:Section xsi:type="ovf:DiskSection_Type">
-    <ovf:Info>Meta-information about the virtual disks</ovf:Info>
-    <ovf:Disk ovf:capacity="1073741824" ovf:diskId="vmdisk1" \
ovf:fileRef="file1" ovf:format=\
"http://www.vmware.com/specifications/vmdk.html#sparse" />
-  </ovf:Section>
   <ovf:Section xsi:type="ovf:NetworkSection_Type">
...
         <rasd:InstanceId>7</rasd:InstanceId>
-        <rasd:ResourceType>17</rasd:ResourceType>
-        <rasd:HostResource>/disk/vmdisk1</rasd:HostResource>
+        <rasd:ResourceType>15</rasd:ResourceType>
+        <rasd:HostResource>/file/file1</rasd:HostResource>
         <rasd:Parent>4</rasd:Parent>
""".format(vmdk_size=self.FILE_SIZE['input.vmdk'],
           iso_size=self.FILE_SIZE['input.iso']))
        # Make sure the old disk is not copied
        self.assertFalse(os.path.exists(os.path.join(self.temp_dir,
                                                     "input.vmdk")),
                         "old disk should be replaced, not exported")
        # Make sure the new disk is copied
        self.assertTrue(filecmp.cmp(self.input_iso,
                                    os.path.join(self.temp_dir, "input.iso")),
                        "new disk should be exported unchanged")

    def test_overwrite_cdrom_with_harddisk(self):
        """Replace a cd-rom with a hard disk."""
        self.command.package = self.input_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.drive_type = 'harddisk'
        self.command.controller = 'ide'
        self.command.address = "1:0"
        self.command.run()
        self.assertLogged(**self.OVERWRITING_FILE)
        self.assertLogged(**self.OVERWRITING_DISK_ITEM)
        self.command.finished()
        self.check_diff("""
     <ovf:File ovf:href="input.vmdk" ovf:id="file1" ovf:size="{vmdk_size}" />
-    <ovf:File ovf:href="input.iso" ovf:id="file2" ovf:size="{iso_size}" />
+    <ovf:File ovf:href="blank.vmdk" ovf:id="file2" ovf:size="{blank_size}" />
     <ovf:File ovf:href="sample_cfg.txt" ovf:id="textfile" \
ovf:size="{cfg_size}" />
...
     <ovf:Disk ovf:capacity="1" ovf:capacityAllocationUnits="byte * 2^30" \
ovf:diskId="vmdisk1" ovf:fileRef="file1" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
+    <ovf:Disk ovf:capacity="512" ovf:capacityAllocationUnits="byte * 2^20" \
ovf:diskId="file2" ovf:fileRef="file2" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
   </ovf:DiskSection>
...
         <rasd:ElementName>CD-ROM 1</rasd:ElementName>
-        <rasd:HostResource>ovf:/file/file2</rasd:HostResource>
+        <rasd:HostResource>ovf:/disk/file2</rasd:HostResource>
         <rasd:InstanceID>7</rasd:InstanceID>
         <rasd:Parent>4</rasd:Parent>
-        <rasd:ResourceType>15</rasd:ResourceType>
+        <rasd:ResourceType>17</rasd:ResourceType>
       </ovf:Item>
        """.format(vmdk_size=self.FILE_SIZE['input.vmdk'],
                   iso_size=self.FILE_SIZE['input.iso'],
                   blank_size=self.FILE_SIZE['blank.vmdk'],
                   cfg_size=self.FILE_SIZE['sample_cfg.txt']))
        # Make sure the old disk is not copied
        self.assertFalse(os.path.exists(os.path.join(self.temp_dir,
                                                     "input.iso")),
                         "old disk should be replaced, not exported")
        # Make sure the new disk is copied
        self.assertTrue(filecmp.cmp(self.blank_vmdk,
                                    os.path.join(self.temp_dir, "blank.vmdk")),
                        "new disk should be exported unchanged")

    def test_disk_conversion(self):
        """Make sure hard disk is converted to stream-optimized VMDK format."""
        # Create a qcow2 image and add it as a new disk
        new_qcow2 = os.path.join(self.temp_dir, "new.qcow2")
        # Make it a small file to keep the test fast
        QCOW2.create_file(path=new_qcow2, capacity="16M")
        self.command.package = self.input_ovf
        self.command.disk_image = new_qcow2
        self.command.controller = 'scsi'
        self.command.run()
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.command.finished()
        # Make sure the disk was converted and added to the OVF
        self.check_diff("""
     <ovf:File ovf:href="sample_cfg.txt" ovf:id="textfile" \
ovf:size="{cfg_size}" />
+    <ovf:File ovf:href="new.vmdk" ovf:id="new.vmdk" ovf:size="{new_size}" />
   </ovf:References>
...
     <ovf:Disk ovf:capacity="1" ovf:capacityAllocationUnits="byte * 2^30" \
ovf:diskId="vmdisk1" ovf:fileRef="file1" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
+    <ovf:Disk ovf:capacity="16" ovf:capacityAllocationUnits="byte * 2^20" \
ovf:diskId="new.vmdk" ovf:fileRef="new.vmdk" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
   </ovf:DiskSection>
...
       </ovf:Item>
+      <ovf:Item>
+        <rasd:AddressOnParent>1</rasd:AddressOnParent>
+        <rasd:ElementName>Hard Disk Drive</rasd:ElementName>
+        <rasd:HostResource>ovf:/disk/new.vmdk</rasd:HostResource>
+        <rasd:InstanceID>14</rasd:InstanceID>
+        <rasd:Parent>3</rasd:Parent>
+        <rasd:ResourceType>17</rasd:ResourceType>
+      </ovf:Item>
     </ovf:VirtualHardwareSection>
""".format(cfg_size=self.FILE_SIZE['sample_cfg.txt'],
           new_size=os.path.getsize(os.path.join(self.temp_dir, "new.vmdk"))))
        # Make sure the disk was actually converted to the right format
        diskrep = DiskRepresentation.from_file(os.path.join(self.temp_dir,
                                                            "new.vmdk"))
        self.assertEqual(diskrep.disk_format, 'vmdk')
        self.assertEqual(diskrep.disk_subformat, "streamOptimized")

    def test_disk_conversion_and_replacement(self):
        """Convert a disk to implicitly replace an existing disk."""
        # Create a qcow2 image and add it as replacement for the existing vmdk
        new_qcow2 = os.path.join(self.temp_dir, "input.qcow2")
        # Keep it small!
        QCOW2.create_file(path=new_qcow2, capacity="16M")
        self.command.package = self.input_ovf
        self.command.disk_image = new_qcow2
        self.command.run()
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.assertLogged(**self.OVERWRITING_FILE)
        self.assertLogged(**self.OVERWRITING_DISK)
        self.assertLogged(**self.OVERWRITING_DISK_ITEM)
        self.command.finished()
        # Make sure the disk was converted and replaced the existing disk
        self.check_diff("""
   <ovf:References>
-    <ovf:File ovf:href="input.vmdk" ovf:id="file1" ovf:size="{input_size}" />
+    <ovf:File ovf:href="input.vmdk" ovf:id="file1" ovf:size="{new_size}" />
     <ovf:File ovf:href="input.iso" ovf:id="file2" ovf:size="{iso_size}" />
...
     <ovf:Info>Virtual disk information</ovf:Info>
-    <ovf:Disk ovf:capacity="1" ovf:capacityAllocationUnits="byte * 2^30" \
ovf:diskId="vmdisk1" ovf:fileRef="file1" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
+    <ovf:Disk ovf:capacity="16" ovf:capacityAllocationUnits="byte * 2^20" \
ovf:diskId="vmdisk1" ovf:fileRef="file1" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
   </ovf:DiskSection>
""".format(input_size=self.FILE_SIZE['input.vmdk'],
           iso_size=self.FILE_SIZE['input.iso'],
           new_size=os.path.getsize(os.path.join(self.temp_dir,
                                                 "input.vmdk"))))

    def test_add_disk_no_existing(self):
        """Add a disk to an OVF that doesn't currently have any.

        Verify correct creation of various OVF sub-sections.
        """
        self.command.package = self.minimal_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.run()
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.assertLogged(**self.CONTROLLER_TYPE_GUESSED_IDE)
        self.assertLogged(**self.ADDRESS_ON_PARENT_NOT_SPECIFIED)
        self.command.finished()
        self.check_diff(file1=self.minimal_ovf,
                        expected="""
 <?xml version='1.0' encoding='utf-8'?>
-<ovf:Envelope xmlns:ovf="http://schemas.dmtf.org/ovf/envelope/1">
-  <ovf:References />
+<ovf:Envelope xmlns:ovf="http://schemas.dmtf.org/ovf/envelope/1" \
xmlns:rasd="http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2/\
CIM_ResourceAllocationSettingData">
+  <ovf:References>
+    <ovf:File ovf:href="blank.vmdk" ovf:id="blank.vmdk" \
ovf:size="{blank_size}" />
+  </ovf:References>
+  <ovf:DiskSection>
+    <ovf:Info>Virtual disk information</ovf:Info>
+    <ovf:Disk ovf:capacity="512" ovf:capacityAllocationUnits="byte * 2^20" \
ovf:diskId="blank.vmdk" ovf:fileRef="blank.vmdk" ovf:format=\
"http://www.vmware.com/interfaces/specifications/vmdk.html#streamOptimized" />
+  </ovf:DiskSection>
   <ovf:VirtualSystem ovf:id="x">
...
       <ovf:Info />
+      <ovf:Item>
+        <rasd:Address>0</rasd:Address>
+        <rasd:Description>IDE Controller 0</rasd:Description>
+        <rasd:ElementName>IDE Controller</rasd:ElementName>
+        <rasd:InstanceID>1</rasd:InstanceID>
+        <rasd:ResourceType>5</rasd:ResourceType>
+      </ovf:Item>
+      <ovf:Item>
+        <rasd:AddressOnParent>0</rasd:AddressOnParent>
+        <rasd:ElementName>Hard Disk Drive</rasd:ElementName>
+        <rasd:HostResource>ovf:/disk/blank.vmdk</rasd:HostResource>
+        <rasd:InstanceID>2</rasd:InstanceID>
+        <rasd:Parent>1</rasd:Parent>
+        <rasd:ResourceType>17</rasd:ResourceType>
+      </ovf:Item>
     </ovf:VirtualHardwareSection>
""".format(blank_size=self.FILE_SIZE['blank.vmdk']))

    @mock.patch("COT.commands.command.available_bytes_at_path")
    def test_add_disk_insufficient_output_space(self, mock_available):
        """Make sure disk space check is invoked when adding a disk."""
        self.command.package = self.minimal_ovf
        self.command.ui.default_confirm_response = False
        # Enough space for the OVF itself, but not for OVF + added disk
        mock_available.return_value = 3 * self.FILE_SIZE['minimal.ovf']
        self.command.disk_image = self.blank_vmdk
        ready, reason = self.command.ready_to_run()
        mock_available.assert_called_once()
        self.assertFalse(ready)
        self.assertRegex(reason, "Insufficient disk space available")

    def test_add_cdrom_to_existing_controller(self):
        """Add a CDROM drive to an existing controller."""
        self.command.package = self.input_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.drive_type = "cdrom"
        self.command.controller = "scsi"
        self.command.address = "0:1"
        self.command.run()
        self.command.finished()
        self.check_diff("""
     <ovf:File ovf:href="sample_cfg.txt" ovf:id="textfile" \
ovf:size="{cfg_size}" />
+    <ovf:File ovf:href="blank.vmdk" ovf:id="blank.vmdk" \
ovf:size="{blank_size}" />
   </ovf:References>
...
       </ovf:Item>
+      <ovf:Item>
+        <rasd:AddressOnParent>1</rasd:AddressOnParent>
+        <rasd:ElementName>CD-ROM Drive</rasd:ElementName>
+        <rasd:HostResource>ovf:/file/blank.vmdk</rasd:HostResource>
+        <rasd:InstanceID>14</rasd:InstanceID>
+        <rasd:Parent>3</rasd:Parent>
+        <rasd:ResourceType>15</rasd:ResourceType>
+      </ovf:Item>
     </ovf:VirtualHardwareSection>
""".format(cfg_size=self.FILE_SIZE['sample_cfg.txt'],
           blank_size=self.FILE_SIZE['blank.vmdk']))

    def test_add_disk_no_room(self):
        """Negative test - add a disk to an OVF whose controllers are full."""
        # iosv.ovf already has two disks. Add a third disk...
        self.command.package = self.iosv_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.run()
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.assertLogged(**self.CONTROLLER_TYPE_GUESSED_IDE)
        self.assertLogged(**self.ADDRESS_ON_PARENT_NOT_SPECIFIED)
        self.command.finished()
        self.check_diff(file1=self.iosv_ovf, expected="""
     <ovf:File ovf:href="input.vmdk" ovf:id="vios-adventerprisek9-m.vmdk" \
ovf:size="152576" />
+    <ovf:File ovf:href="blank.vmdk" ovf:id="blank.vmdk" \
ovf:size="{blank_size}" />
   </ovf:References>
...
     <ovf:Disk ovf:capacity="1073741824" ovf:capacityAllocationUnits="byte" \
ovf:diskId="vios-adventerprisek9-m.vmdk" \
ovf:fileRef="vios-adventerprisek9-m.vmdk" \
ovf:format="http://www.vmware.com/interfaces/specifications/\
vmdk.html#streamOptimized" />
+    <ovf:Disk ovf:capacity="512" ovf:capacityAllocationUnits="byte * 2^20" \
ovf:diskId="blank.vmdk" ovf:fileRef="blank.vmdk" \
ovf:format="http://www.vmware.com/interfaces/specifications/\
vmdk.html#streamOptimized" />
   </ovf:DiskSection>
...
       </ovf:Item>
+      <ovf:Item>
+        <rasd:Address>1</rasd:Address>
+        <rasd:Description>IDE Controller 1</rasd:Description>
+        <rasd:ElementName>IDE Controller</rasd:ElementName>
+        <rasd:InstanceID>6</rasd:InstanceID>
+        <rasd:ResourceSubType>virtio</rasd:ResourceSubType>
+        <rasd:ResourceType>5</rasd:ResourceType>
+      </ovf:Item>
+      <ovf:Item>
+        <rasd:AddressOnParent>0</rasd:AddressOnParent>
+        <rasd:ElementName>Hard Disk Drive</rasd:ElementName>
+        <rasd:HostResource>ovf:/disk/blank.vmdk</rasd:HostResource>
+        <rasd:InstanceID>7</rasd:InstanceID>
+        <rasd:Parent>6</rasd:Parent>
+        <rasd:ResourceType>17</rasd:ResourceType>
+      </ovf:Item>
       <ovf:Item ovf:required="false">
""".format(blank_size=self.FILE_SIZE['blank.vmdk']))

        # Add a fourth disk...
        self.command.package = self.temp_file
        self.command.disk_image = self.input_iso
        self.command.run()
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_CDROM)
        self.assertLogged(**self.CONTROLLER_TYPE_GUESSED_IDE)
        self.command.finished()
        self.check_diff(file1=self.iosv_ovf, expected="""
     <ovf:File ovf:href="input.vmdk" ovf:id="vios-adventerprisek9-m.vmdk" \
ovf:size="152576" />
+    <ovf:File ovf:href="blank.vmdk" ovf:id="blank.vmdk" \
ovf:size="{blank_size}" />
+    <ovf:File ovf:href="input.iso" ovf:id="input.iso" ovf:size="{iso_size}" />
   </ovf:References>
...
     <ovf:Disk ovf:capacity="1073741824" ovf:capacityAllocationUnits="byte" \
ovf:diskId="vios-adventerprisek9-m.vmdk" \
ovf:fileRef="vios-adventerprisek9-m.vmdk" ovf:format="http://www.vmware.com/\
interfaces/specifications/vmdk.html#streamOptimized" />
+    <ovf:Disk ovf:capacity="512" ovf:capacityAllocationUnits="byte * 2^20" \
ovf:diskId="blank.vmdk" ovf:fileRef="blank.vmdk" \
ovf:format="http://www.vmware.com/interfaces/specifications/\
vmdk.html#streamOptimized" />
   </ovf:DiskSection>
...
       </ovf:Item>
+      <ovf:Item>
+        <rasd:Address>1</rasd:Address>
+        <rasd:Description>IDE Controller 1</rasd:Description>
+        <rasd:ElementName>IDE Controller</rasd:ElementName>
+        <rasd:InstanceID>6</rasd:InstanceID>
+        <rasd:ResourceSubType>virtio</rasd:ResourceSubType>
+        <rasd:ResourceType>5</rasd:ResourceType>
+      </ovf:Item>
+      <ovf:Item>
+        <rasd:AddressOnParent>0</rasd:AddressOnParent>
+        <rasd:ElementName>Hard Disk Drive</rasd:ElementName>
+        <rasd:HostResource>ovf:/disk/blank.vmdk</rasd:HostResource>
+        <rasd:InstanceID>7</rasd:InstanceID>
+        <rasd:Parent>6</rasd:Parent>
+        <rasd:ResourceType>17</rasd:ResourceType>
+      </ovf:Item>
+      <ovf:Item>
+        <rasd:AddressOnParent>1</rasd:AddressOnParent>
+        <rasd:ElementName>CD-ROM Drive</rasd:ElementName>
+        <rasd:HostResource>ovf:/file/input.iso</rasd:HostResource>
+        <rasd:InstanceID>8</rasd:InstanceID>
+        <rasd:Parent>6</rasd:Parent>
+        <rasd:ResourceType>15</rasd:ResourceType>
+      </ovf:Item>
       <ovf:Item ovf:required="false">
""".format(blank_size=self.FILE_SIZE['blank.vmdk'],
           iso_size=self.FILE_SIZE['input.iso']))

        # Create a qcow2 image
        new_qcow2 = os.path.join(self.temp_dir, "foozle.qcow2")
        # Keep it small!
        QCOW2.create_file(path=new_qcow2, capacity="16M")
        # Try to add a fifth disk - IDE controllers are full!
        self.command.package = self.temp_file
        self.command.disk_image = new_qcow2
        self.assertRaises(ValueTooHighError, self.command.run)
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.assertLogged(**self.CONTROLLER_TYPE_GUESSED_IDE)

    def test_overwrite_implicit_file_id(self):
        """file_id defaults to filename if not set."""
        self.command.package = self.invalid_ovf
        self.command.disk_image = self.input_vmdk
        self.command.run()
        self.assertLogged(**self.UNRECOGNIZED_PRODUCT_CLASS)
        self.assertLogged(**self.NONEXISTENT_FILE)
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.assertLogged(**self.CONTROLLER_TYPE_GUESSED_IDE)
        self.assertLogged(**self.OVERWRITING_FILE)
        self.assertLogged(**self.OVERWRITING_DISK)
        self.command.finished()
        self.assertLogged(**self.invalid_hardware_warning(
            "howlongofaprofilenamecanweusehere", "0", "MiB of RAM"))
        self.assertLogged(msg="Removing unused network")
        self.check_diff(file1=self.invalid_ovf, expected="""
   <ovf:References>
-    <ovf:File ovf:href="this_is_a_really_long_filename_for_a_disk.vmdk" \
ovf:id="input.vmdk" ovf:size="{input_size}" />
+    <ovf:File ovf:href="input.vmdk" ovf:id="input.vmdk" \
ovf:size="{input_size}" />
     <ovf:File ovf:href="input.iso" ovf:id="input.iso" ovf:size="360448" />
...
     </ovf:Network>
-    <ovf:Network ovf:name="name-but-no-description" />
   </ovf:NetworkSection>
...
       </ovf:Item>
+      <ovf:Item>
+        <rasd:AddressOnParent>1</rasd:AddressOnParent>
+        <rasd:ElementName>Hard Disk Drive</rasd:ElementName>
+        <rasd:HostResource>ovf:/disk/input.vmdk</rasd:HostResource>
+        <rasd:InstanceID>6</rasd:InstanceID>
+        <rasd:Parent>1</rasd:Parent>
+        <rasd:ResourceType>17</rasd:ResourceType>
+      </ovf:Item>
       <ovf:Item ovf:configuration="myprofile">
        """.format(input_size=self.FILE_SIZE['input.vmdk']))
        # ovftool will fail because invalid_ovf has an invalid Disk fileRef
        self.validate_output_with_ovftool = False

    def test_overwrite_disk_with_bad_host_resource(self):
        """Negative test - invalid HostResource value in OVF."""
        self.command.package = self.invalid_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.controller = "ide"
        self.command.address = "0:0"
        with self.assertRaises(ValueUnsupportedError) as catcher:
            self.command.run()
        self.assertTrue(re.search("HostResource", str(catcher.exception)))
        self.assertLogged(**self.UNRECOGNIZED_PRODUCT_CLASS)
        self.assertLogged(**self.NONEXISTENT_FILE)
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
        self.assertLogged(levelname='ERROR',
                          msg="Unrecognized HostResource format")

    def test_overwrite_disk_with_bad_parent_by_file(self):
        """Negative test - invalid parent for disk, identified by filename."""
        self.command.package = self.invalid_ovf
        self.command.disk_image = self.input_iso
        self.assertRaises(LookupError, self.command.run)
        self.assertLogged(**self.UNRECOGNIZED_PRODUCT_CLASS)
        self.assertLogged(**self.NONEXISTENT_FILE)
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_CDROM)

    def test_overwrite_disk_with_bad_parent_by_fileid(self):
        """Negative test - invalid parent for disk, identified by fileid."""
        self.command.package = self.invalid_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.file_id = "input.iso"
        self.assertRaises(LookupError, self.command.run)
        self.assertLogged(**self.UNRECOGNIZED_PRODUCT_CLASS)
        self.assertLogged(**self.NONEXISTENT_FILE)
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)

    def test_overwrite_disk_with_bad_fileref(self):
        """Negative test - invalid fileref in OVF."""
        self.command.package = self.invalid_ovf
        self.command.disk_image = self.blank_vmdk
        self.command.file_id = "flash2"
        self.assertRaises(LookupError, self.command.run)
        self.assertLogged(**self.UNRECOGNIZED_PRODUCT_CLASS)
        self.assertLogged(**self.NONEXISTENT_FILE)
        self.assertLogged(**self.DRIVE_TYPE_GUESSED_HARDDISK)
