# S16 Update process summary

## Update Models

I created three update models. 

- <a href="S16 image update model.md">System update using a new image created by yocto.</a>
- <a href="S16 package update model.md">System update using a package manager.</a>
- <a href="S16 application stack update.md">Application stack update using nuget package manager.</a>

## Thoughts on the update process

When using a package manager we need to decide if we want to use packages provided by a distribution, or we want to create our own managed package repository. If we want to use packages by a distribution we need to consider using this distribution as base and not Yocto, because Yocto is more of an image based system. And i don't know how that mingles with distribution packages. I think i read somewhere that with yocto you can use debian as a base instead of their own poky distribution. But more research is needed.
Yocto has support for 3 types of package managers.

- 'package_deb' for debian style deb files
- 'package_ipk' for ipk files are used by opkg (a debian style embedded package manager)
- 'package_rpm' for rpm style packages

## Different update channels

We should consider creating different update channels for different purposes. For example a beta channel for testing new features, a normal channel, and perhaps different channels for certain products.

## Distributed updates

We should consider using an uneven update distribution. For example first deploy the update for 1% of devices with dignostics enabled. Then when there are no problems go to 10% and so on. This way we can catch problems early and not deploy a broken update to all devices.

## What happens if an update reroll fails

These modeled cases are not considering what to do if a reroll of an update fails. I didn't include it because we need to decide
if in this case we want to make a factory reset, or just inform the user.
