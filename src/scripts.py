SCRIPTS = [
	{
		"title": "Updates",
		"icon-name": "updates-symbolic",
		"sections": [
			{
			"title":  "Pacman",
			"subtitle": "Some useful operations you can do with Arch Linux package manager",
			"scripts":
				[
					{
						"title": "Run full System Update",
						"subtitle": "Update the system and all of its packages",
						"command": "sudo pacman -Syu;exec bash",
						"description": "sudo pacman -Syu",
					},
					{
						"title": "Force refresh packages list",
						"subtitle": "Mirrors can be out of sync, use this command to resyncronize them",
						"command": "sudo pacman -Syyu; exec bash",
						"description": "sudo pacman -Syyu",
					},
					{
						"title": "Update mirrorlist",
						"subtitle": "Will update the mirrorlist for faster downloads using pacman",
						"command": "sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak;sudo reflector --verbose --latest 10 --protocol https --sort rate --save /etc/pacman.d/mirrorlist; exec bash",
						"description": "sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak\nsudo reflector --verbose --latest 10 --protocol https --sort rate --save /etc/pacman.d/mirrorlist",
					},
					{
						"title": "Restore old mirrorlist",
						"subtitle": "Restore old mirrorlist if mirrorlist update failed",
						"command": "sudo rm -rf /etc/pacman.d/mirrorlist; sudo cp /etc/pacman.d/mirrorlist.bak /etc/pacman.d/mirrorlist; exec bash",
						"description": "sudo rm -rf /etc/pacman.d/mirrorlist\nsudo cp /etc/pacman.d/mirrorlist.bak /etc/pacman.d/mirrorlist",
					},
					{
						"title": "Refresh Keyring",
						"subtitle": "Refresh pacman Keyring, usually, it is very rarely needed and a pretty long operation",
						"command": "sudo pacman-key --refresh-keys;exec bash",
						"description": "sudo pacman-key --refresh-keys",
					},
				]
			},
			{
			"title":  "Nyarch Applications",
			"subtitle": "Nyarch linux applications are not automatically updated, use this section to update them",
			"scripts":
				[
					{
						"title": "Update Nyarch Tour",
						"subtitle": "Update Nyarch Tour application by downloading it from the latest release on github",
						"command": "cd /tmp; wget https://github.com/nyarchlinux/nyarchtour/releases/latest/download/nyarchtour.flatpak; flatpak install nyarchtour.flatpak;exec bash",
						"description": "cd /tmp\nwget https://github.com/nyarchlinux/nyarchtour/releases/latest/download/nyarchtour.flatpak\nflatpak install nyarchtour.flatpak",
					},
					{
						"title": "Update Nyarch Customize",
						"subtitle": "Update Nyarch Customize application by downloading it from the latest release on github",
						"command": "cd /tmp; wget https://github.com/nyarchlinux/nyarchcustomize/releases/latest/download/nyarchcustomize.flatpak; flatpak install nyarchcustomize.flatpak;exec bash",
						"description": "cd /tmp\nwget https://github.com/nyarchlinux/nyarchcustomize/releases/latest/download/nyarchcustomize.flatpak\nflatpak install nyarchcustomize.flatpak",
					},
					{
						"title": "Update Nyarch Wizard",
						"subtitle": "Update Nyarch Wizard application by downloading it from the latest release on github",
						"command": "cd /tmp; wget https://github.com/nyarchlinux/nyarchwizard/releases/latest/download/wizard.flatpak; flatpak install wizard.flatpak;exec bash",
						"description": "cd /tmp\nwget https://github.com/nyarchlinux/nyarchwizard/releases/latest/download/wizard.flatpak\nflatpak install wizard.flatpak",
					},
					{
						"title": "Update Catgirl Downloader",
						"subtitle": "Update Catgirl Downloader application by downloading it from the latest release on github",
						"command": "cd /tmp; wget https://github.com/nyarchlinux/catgirldownloader/releases/latest/download/catgirldownloader.flatpak; flatpak install catgirldownloader.flatpak;exec bash",
						"description": "cd /tmp\nwget https://github.com/nyarchlinux/catgirldownloader/releases/latest/download/catgirldownloader.flatpak\nflatpak install catgirldownloader.flatpak",
					},
					{
						"title": "Update Nyarch Script",
						"subtitle": "Update Nyarch Script application by downloading it from the latest release on github",
						"command": "cd /tmp; wget https://github.com/nyarchlinux/nyarchscript/releases/latest/download/nyarchscript.flatpak; flatpak install nyarchscript.flatpak;exec bash",
						"description": "cd /tmp\nwget https://github.com/nyarchlinux/nyarchscript/releases/latest/download/nyarchscript.flatpak\nflatpak install nyarchscript.flatpak",
					},
					{
						"title": "Update NyarcMenu",
						"subtitle": "Update NyarcMenu extension, the Gnome extension that manages menu",
						"command": "cd /tmp; git clone https://github.com/NyarchLinux/NyarcMenu.git; cd NyarcMenu; make install; exec bash",
						"description": "cd /tmp\ngit clone https://github.com/NyarchLinux/NyarcMenu.git\ncd NyarcMenu\nmake install",
					},
				]
			}
		]
	},
	{
		"title": "Install",
		"icon-name": "palette-symbolic",
		"sections": [
			{
			"title":  "Command-line Utilities",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Install fish",
						"subtitle": "This command installs fish and sets it as default shell",
						"command": "sudo pacman -S fish;chsh -s $(which fish); exec fish",
						"description": "sudo pacman -S fish & chsh fish",
					},
					{
						"title": "Install Oh My Fish!",
						"subtitle": "This command installs Oh My Fish to tweak fish easily",
						"command": "curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish;exec fish",
						"description": "curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish",
					},
				]
			},
			{
			"title":  "Performance",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Install preload",
						"subtitle": "Makes applications run faster by prefetching binaries and shared objects",
						"command": "trizen -S preload; sudo systemctl enable preload; exec bash",
						"description": "trizen -S preload\nsudo systemctl enable preload",
					},
					{
						"title": "Install auto-cpufreq",
						"website": "xdg-open https://github.com/AdnanHodzic/auto-cpufreq",
						"subtitle": "Automatic CPU speed and power optimizer, useful to henance laptop battery life",
						"command": "trizen -S auto-cpufreq;exec bash",
						"description": "trizen -S auto-cpufreq | bash",
					},
				]
			},
			{
			"title":  "Kernels",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Install Linux Zen Kernel",
						"subtitle": "This command installs linux zen kernel, optimized for desktop, you can choose which kernel to boot from GRUB in 'advanced options'",
						"command": "sudo pacman -S linux-zen linux-zen-headers;exec fish",
						"description": "sudo pacman -S linux-zen linux-zen-headers | fish",
					},
					{
						"title": "Install Linux LTS Kernel",
						"subtitle": "This command installs linux Long Term Support kernel, useful if you have issues with proprietary drivers, you can choose which kernel to boot from GRUB in 'advanced options'",
						"command": "sudo pacman -S linux-lts linux-lts-headers;exec fish",
						"description": "sudo pacman -S linux-lts linux-lts-headers | fish",
					},
				]
			},
			{
			"title":  "Themes",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Firefox Gnome Theme",
						"website": "xdg-open https://github.com/rafaelmardojai/firefox-gnome-theme",
						"subtitle": "Make firefox more coherent with your desktop",
						"command": "cd /tmp; git clone https://github.com/rafaelmardojai/firefox-gnome-theme; cd firefox-gnome-theme; bash scripts/auto-install.sh; exec bash",
						"description": "cd /tmp\ngit clone https://github.com/rafaelmardojai/firefox-gnome-theme\ncd firefox-gnome-theme\n./scripts/auto-install.sh",
					},
					{
						"title": "Discord Dnome Theme",
						"website": "xdg-open https://github.com/NyarchLinux/NyarchScript/tree/master/docs/DNOME.md",
						"subtitle": "Make discord more coherent with your desktop, this command will also install crycord to inject css",
						"command": "trizen -S crycord; mkdir -p ~/.config/discord-themes; cd ~/.config/discord-themes; wget https://github.com/GeopJr/DNOME/blob/main/DNOME-latest.css; crycord -c ~/.config/discord-themes/DNOME-latest.css",
						"description": "trizen -S crycord  # Install Crycord from the AUR\nmkdir -p ~/.config/discord-themes\ncd ~/.config/discord-themes\nwget https://github.com/GeopJr/DNOME/blob/main/DNOME-latest.css  # Download css theme\ncrycord -c ~/.config/discord-themes/DNOME-latest.css  # Inject CSS",
					},
				]
			},
			{
			"title":  "Extra",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Install nvidia drivers",
						"subtitle": "Install nvidia drivers, not needed on nvidia ISO builds",
						"command": "sudo pacman -S nvidia nvidia-libgl; echo 'Reboot to install drivers';exec bash",
						"description": "sudo pacman -S nvidia nvidia-libgl",
					},
					{
						"title": "Wacom drivers",
						"subtitle": "Install wacom drivers for graphics tablets and stylus",
						"command": "sudo pacman -S xf86-input-wacom libwacom;trizen -S input-wacom-dkms wacom-utility;exec bash",
						"description": "sudo pacman -S xf86-input-wacom libwacom",
					},
					{
						"title": "Wacom drivers for Surface devices",
						"subtitle": "Install a patched version of libwacom for Surface devices",
						"command": "trizen -S libwacom-surface;exec bash",
						"description": "trizen -S libwacom-surface",
					},
				]
			}
		]
	},
	{
		"title": "Tweaks",
		"icon-name": "tweaks-symbolic",
		"sections": [
			{
			"title":  "Touchscreen scripts",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Make firefox use Wayland",
						"subtitle": "Do not run this command if you are using X11, check the script in info section of Nyarch Script to know if you are using it. Enhances Firefox perfomances under wayland.",
						"command": "cd /usr/share; sudo rm -rf firefox.desktop;sudo wget https://raw.githubusercontent.com/NyarchLinux/NyarchScript/master/docs/firefox.desktop; sudo chmod +x firefox.desktop;exec bash",
						"description": "cd /usr/share\nsudo rm -rf firefox.desktop\nsudo wget https://raw.githubusercontent.com/NyarchLinux/NyarchScript/master/docs/firefox.desktop\nsudo chmod +x firefox.desktop",
					},
					{
						"title": "Fix firefox on touchscreen",
						"subtitle": "This command will fix firefox gestures on touchscreens",
						"command": "echo export MOZ_USE_XINPUT2=1 | sudo tee /etc/profile.d/use-xinput2.sh;exec bash",
						"description": "echo export MOZ_USE_XINPUT2=1 | sudo tee /etc/profile.d/use-xinput2.sh",
					},
					{
						"title": "Install osk/touchpad extension",
						"subtitle": "Useful on some 2 in 1, this extension enables On Screen Keyboard from accessibility settings when touchpad is turned off and viceversa",
						"command": "cd ~/.config/local/share/gnome-shell/extensions;git clone https://github.com/FrancescoCaracciolo/OSK-Touchpad-inverse-toggle-Gnome-Ext.git;exec bash",
						"description": "cd ~/.config/local/share/gnome-shell/extensions\ngit clone https://github.com/FrancescoCaracciolo/OSK-Touchpad-inverse-toggle-Gnome-Ext.git",
					},
				]
			},
		]
	},
	{
		"title": "Information",
		"icon-name": "info-symbolic",
		"sections": [
			{
			"title":  "Command to get information about your system",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Run nyaofetch",
						"subtitle": "This command will show you your general system information",
						"command": "nyaofetch;exec bash",
						"description": "nyaofetch",
					},
					{
						"title": "Run btop",
						"subtitle": "This command will show an overall interface with your system resources information",
						"command": "btop;exec bash",
						"description": "btop",
					},
					{
						"title": "Check temperatures",
						"subtitle": "This command will show you your system temperatures",
						"command": "sensors;exec bash",
						"description": "sensors",
					},
					{
						"title": "Check if running on Wayland",
						"subtitle": "This command will tell you x11 if running on Xorg, Wayland if running on wayland",
						"command": "echo $XDG_SESSION_TYPE;exec bash",
						"description": "echo $XDG_SESSION_TYPE",
					},
				]
			},
		]
	}








]
