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
						"command": "sudo pacman -Syu;sudo flatpak update; exec bash",
						"description": "sudo pacman -Syu",
					},
					{
						"title": "Force refresh packages list",
						"subtitle": "Mirrors can be out of sync, use this command to resyncronize them",
						"command": "sudo pacman -Syyu; exec bash",
						"description": "sudo pacman -Syyu",
					},
					{
						"title": "Refresh Pacman keys",
						"subtitle": "NOTE: Takes some time. In case there are problems with keys, you can refresh every pacman key",
						"command": "sudo pacman-key --refresh-keys; exec bash",
						"description": "sudo pacman-key --refresh-keys",
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
						"title": "Remove db lock",
						"subtitle": "Remove pacman db lock in case of errors.",
						"command": "sudo rm -rf  /var/lib/pacman/db.lck; exec bash",
						"description": "sudo rm -rf  /var/lib/pacman/db.lck",
					},
				]
			},
			{
			"title":  "Nyarch Applications",
			"subtitle": "Nyarch linux applications are not automatically updated, use this section to update them",
			"scripts":
				[
					{
						"title": "Update Nyarch Assistant",
						"subtitle": "Update Nyarch Assistant application by downloading it from the latest release on github",
						"command": "cd /tmp; wget https://github.com/nyarchlinux/nyarchassistant/releases/latest/download/nyarchassistant.flatpak; flatpak install nyarchassistant.flatpak;exec bash",
						"description": "cd /tmp\nwget https://github.com/nyarchlinux/nyarchassistant/releases/latest/download/nyarchassistant.flatpak\nflatpak install nyarchassistant.flatpak",
					},
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
						"title": "Update Waifu Downloader",
						"subtitle": "Update Waifu Downloader application by downloading it from the latest release on github",
						"command": "cd /tmp; wget https://github.com/nyarchlinux/waifudownloader/releases/latest/download/waifudownloader.flatpak; flatpak install waifudownloader.flatpak;exec bash",
						"description": "cd /tmp\nwget https://github.com/nyarchlinux/waifudownloader/releases/latest/download/waifudownloader.flatpak\nflatpak install waifudownloader.flatpak",
					},
					{
						"title": "Update Nyarch Script",
						"subtitle": "Update Nyarch Script application by downloading it from the latest release on github",
						"command": "cd /tmp; wget https://github.com/nyarchlinux/nyarchscript/releases/latest/download/nyarchscript.flatpak; flatpak install nyarchscript.flatpak;exec bash",
						"description": "cd /tmp\nwget https://github.com/nyarchlinux/nyarchscript/releases/latest/download/nyarchscript.flatpak\nflatpak install nyarchscript.flatpak",
					},
					{
						"title": "Update Material You",
						"subtitle": "Update Material You extension, the Gnome extension that manages Material You",
						"command": "cd /tmp; git clone https://github.com/FrancescoCaracciolo/material-you-colors.git; cd material-you-colors; make build;make install; npm install --prefix $HOME/.local/share/gnome-shell/extensions/material-you-colors@francescocaracciolo.github.io; exec bash",
						"description": "cd /tmp\ngit clone https://github.com/FrancescoCaracciolo/material-you-colors.git\ncd material-you-colors\nmake build\nmake install\nnpm install --prefix $HOME/.local/share/gnome-shell/extensions/material-you-colors@francescocaracciolo.github.io;",
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
						"description": "sudo pacman -S fish\nchsh -s $(which fish); exec fish",
					},
					{
						"title": "Install Oh My Fish!",
						"website": "xdg-open https://github.com/oh-my-fish/oh-my-fish#Getting-Started",
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
						"command": "yay -S preload; sudo systemctl enable --now preload; exec bash",
						"description": "yay -S preload\nsudo systemctl enable --now preload",
					},
					{
						"title": "Install auto-cpufreq",
						"website": "xdg-open https://github.com/AdnanHodzic/auto-cpufreq",
						"subtitle": "Automatic CPU speed and power optimizer, useful to enhance laptop battery life",
						"command": "yay -S auto-cpufreq;exec bash",
						"description": "yay -S auto-cpufreq",
					},
					{
						"title": "Install power-profiles-daemon",
						"subtitle": "Power Profiles daemon modifies system behaviour based upon user-selected power profiles, choosen from quick settings",
						"command": "sudo pacman -S power-profiles-daemon;exec bash",
						"description": "sudo pacman -S power-profiles-daemon",
					},
				]
			},
			{
			"title":  "Kernels",
			"subtitle": "After installing, select your preferred kernel in grub advanced options",
			"scripts":
				[
					{
						"title": "Install Linux Zen Kernel",
						"subtitle": "This command installs linux zen kernel, optimized for desktop, you can choose which kernel to boot from GRUB in 'advanced options'",
						"command": "sudo pacman -S linux-zen linux-zen-headers;exec bash",
						"description": "sudo pacman -S linux-zen linux-zen-headers",
					},
					{
						"title": "Install Linux LTS Kernel",
						"subtitle": "This command installs linux Long Term Support kernel, useful if you have issues with proprietary drivers, you can choose which kernel to boot from GRUB in 'advanced options'",
						"command": "sudo pacman -S linux-lts linux-lts-headers;exec bash",
						"description": "sudo pacman -S linux-lts linux-lts-headers",
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
						"title": "Uninstall Firefox Gnome theme",
						"website": "xdg-open https://github.com/rafaelmardojai/firefox-gnome-theme#uninstalling",
						"subtitle": "Uninstall Firefox Gnome Theme",
						"command": "xdg-open https://github.com/rafaelmardojai/firefox-gnome-theme#uninstalling",
						"description": "https://github.com/rafaelmardojai/firefox-gnome-theme#uninstalling",
					},
					{
						"title": "Discord Dnome Theme",
						"website": "xdg-open https://github.com/NyarchLinux/NyarchScript/tree/master/docs/DNOME.md",
						"subtitle": "Make discord more coherent with your desktop, this command will also install crycord to inject css",
						"command": "yay -S crycord; mkdir -p ~/.config/discord-themes; cd ~/.config/discord-themes; wget https://raw.githubusercontent.com/GeopJr/DNOME/main/DNOME-latest.css; crycord -c ~/.config/discord-themes/DNOME-latest.css;exec bash",
						"description": "yay -S crycord  # Install Crycord from the AUR\nmkdir -p ~/.config/discord-themes\ncd ~/.config/discord-themes\nwget https://raw.githubusercontent.com/GeopJr/DNOME/main/DNOME-latest.css  # Download css theme\ncrycord -c ~/.config/discord-themes/DNOME-latest.css  # Inject CSS",
					},
					{
						"title": "Uninstall Discord Dnome Theme",
						"subtitle": "Uninstall dnome theme from discord",
						"command": "crycord -r; exec bash",
						"description": "crycord -r",
					},
					{
						"title": "Install Pywalfox",
						"subtitle": "Adapts firefox theme color to NyarchLinux theme",
						"command": "yay -S python-pywalfox; pywalfox install; xdg-open https://addons.mozilla.org/it/firefox/addon/pywalfox/; exec bash",
						"website": "xdg-open https://addons.mozilla.org/it/firefox/addon/pywalfox/",
						"description": "yay -S python-pywalfox\npywalfox install\nxdg-open https://addons.mozilla.org/it/firefox/addon/pywalfox/",
					},
					{
						"title": "Install Wal VSCode Theme",
						"subtitle": "Adapts VSCode theme color to NyarchLinux theme",
						"command": "xdg-open https://marketplace.visualstudio.com/items?itemName=dlasagno.wal-theme",
						"website": "xdg-open https://marketplace.visualstudio.com/items?itemName=dlasagno.wal-theme",
						"description": "xdg-open https://marketplace.visualstudio.com/items?itemName=dlasagno.wal-theme",
					},
				]
			},
			{
			"title":  "Drivers",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Install nvidia drivers",
						"subtitle": "Open the installation guide for nvidia drivers",
						"command": "xdg-open https://github.com/korvahannu/arch-nvidia-drivers-installation-guide",
						"description": "xdg-open https://github.com/korvahannu/arch-nvidia-drivers-installation-guide",
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
						"command": "yay -S libwacom-surface;exec bash",
						"description": "yay -S libwacom-surface",
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
		        "title": "Maintenance scripts",
		        "subtitle": None,
		        "scripts":
		            [
		                {
		                    "title": "Enable Bluetooth Service",
		                    "subtitle": "Make bluetooth work",
		                    "command": "sudo systemctl enable --now bluetooth.service;exec bash",
		                    "description": "sudo systemctl enable --now bluetooth.service"
		                },
		                {
		                    "title": "Cleanup journal space",
		                    "subtitle": "Cleanup jorunalctl logs before the last two weeks to free up space",
		                    "command": "sudo journalctl --vacuum-time=2weeks;exec bash",
		                    "description": "sudo journalctl --vacuum-time=2weeks"
		                },
		                {
		                    "title": "Clean package cache",
		                    "subtitle": "Remove pacman package caches to free up space",
		                    "command": "sudo pacman -Scc;exec bash",
		                    "description": "sudo pacman -Scc"
		                },
		                {
		                    "title": "Reset all pacman keys",
		                    "subtitle": "NOTE: Might take some minutes. Reset pacman keys, useful if you are having errors updating the system because of some keys missing/package corrupted",
		                    "command": "sudo rm /var/lib/pacman/sync/*; sudo rm -rf /etc/pacman.d/gnupg/*; sudo pacman-key --init; sudo pacman-key --populate; sudo pacman -S --noconfirm archlinux-keyring;exec bash",
		                    "description": "sudo rm /var/lib/pacman/sync/*\nsudo rm -rf /etc/pacman.d/gnupg/*\nsudo pacman-key --init\nsudo pacman-key --populate\nsudo pacman -S --noconfirm archlinux-keyring"
		                }
		            ]
		    },
			{
			"title":  "Touchscreen scripts",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Install screen autorotate extension",
						"subtitle": "Enable screen rotation regardless of touch mode.",
						"command": "cd /tmp; git clone https://github.com/shyzus/gnome-shell-extension-screen-autorotate.git; mv gnome-shell-extension-screen-autorotate/screen-rotate@shyzus.github.io ~/.local/share/gnome-shell/extensions/;exec bash",
						"description": "cd /tmp\ngit clone https://github.com/shyzus/gnome-shell-extension-screen-autorotate.git\nmv gnome-shell-extension-screen-autorotate/screen-rotate@shyzus.github.io ~/.local/share/gnome-shell/extensions/",
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
