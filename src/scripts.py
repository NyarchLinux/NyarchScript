SCRIPTS = [
	{
		"title": "Updates",
		"icon-name": "audio-volume-high-symbolic",
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
						"title": "Refresh Keyring",
						"subtitle": "Refresh pacman Keyring, usually, it is very rarely needed and a pretty long operation",
						"command": "pacman-key --refresh-keys;exec bash",
						"description": "pacman-key --refresh-keys",
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
						"title": "Update Nyarch Wizard",
						"subtitle": "Update Nyarch Wizard application by downloading it from the latest release on github",
						"command": "cd /tmp; wget https://github.com/nyarchlinux/nyarchwizard/releases/latest/download/nyarchwizard.flatpak; flatpak install nyarchwizard.flatpak;exec bash",
						"description": "cd /tmp\nwget https://github.com/nyarchlinux/nyarchwizard/releases/latest/download/nyarchwizard.flatpak\nflatpak install nyarchwizard.flatpak",
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
		"icon-name": "audio-volume-high-symbolic",
		"sections": [
			{
			"title":  "Command-line Utilities",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Install fish",
						"subtitle": "This command installs fish and sets it as default shell",
						"command": "sudo pacman -S fish;exec bash",
						"description": "sudo pacman -S fish & chsh fish",
					},
				]
			},
			{
			"title":  "Themes",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Install GRUB theme",
						"subtitle": "This command installs fish and sets it as default shell",
						"command": "",
						"description": "",
					},
				]
			}
		]
	},
	{
		"title": "Tweaks",
		"icon-name": "audio-volume-high-symbolic",
		"sections": [
			{
			"title":  "Touchscreen scripts",
			"subtitle": None,
			"scripts":
				[
					{
						"title": "Fix firefox on touchscreen",
						"subtitle": "This command installs fish and sets it as default shell",
						"command": "sudo pacman -S fish;exec bash",
						"description": "sudo pacman -S fish & chsh fish",
					},
				]
			},
		]
	}








]
