I grew tired of having to use my phone to authenticate my logins, so I wrote this tool as a substitute. It's missing some of my 2FA logins (either because I just haven't added them or I was unable to retrieve their secret key).

My original 2FA authenticator was a command-line program, but I decided to create a GUI with PyQt5 to become more acquainted with the library, seeing as most of my Python GUI experience lies with Tkinter.

At some point I would like to provide this tool with the capability to add new 2FA code generators right through the GUI, as well as encrypt and store their secret keys. If possible, I would also like to add a feature that can scan QR codes on the screen to negate the need for typing or copying/pasting secret keys altogether.