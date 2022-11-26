from service import watcher, config, log


def run_main():
    watcher.init()


if __name__ == '__main__':
    log.info("app booting up")

    config.create_config()
    log.info("config created")

    run_main()
