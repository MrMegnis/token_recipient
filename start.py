import daemon

import main
from tg import bot

with daemon.DaemonContext():
    main.app.run()
    bot.start_bot()