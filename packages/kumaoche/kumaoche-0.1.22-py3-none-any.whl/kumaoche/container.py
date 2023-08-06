# -*- coding: utf-8 -*-

from .config import ConfigParser, ServiceConfig
from .exec_env import DisableEnv, Shell, Docker, StringBuilder
from .service import PackageManager
from .runner import InvokeRunner


class Container(object):

    @staticmethod
    def env(config: ServiceConfig):
        if config.env == 'string_builder':
            return StringBuilder(config.string_builder, config.environment, InvokeRunner)
        elif config.env == 'shell':
            return Shell(config.shell, config.environment, InvokeRunner)
        elif config.env == 'docker':
            return Docker(config.docker, config.environment, InvokeRunner)
        else:
            return DisableEnv()

    @classmethod
    def all_repository_names(cls):
        return ConfigParser.all_repository_names()

    @classmethod
    def find_services(cls, repository_name: str):
        services = []

        for config in ConfigParser.find(repository_name):
            for service in config.services:
                services.extend([PackageManager(cls.env(service), service)])

        return services

    @classmethod
    def find_services_by_name(cls, repository_name: str, service_lang_name: str):
        services = []

        for config in ConfigParser.find(repository_name):
            for service in config.services:
                if service.name() == service_lang_name:
                    services.extend([PackageManager(cls.env(service), service)])

        return services

    @classmethod
    def find_all_services(cls):
        services = []

        for role in ConfigParser.all_repository_names():
            for config in ConfigParser.find(role):
                for service in config.services:
                    services.extend([PackageManager(cls.env(service), service)])

        return services

    @classmethod
    def find_all_services_by_name(cls, service_lang_name: str):
        services = []

        for role in ConfigParser.all_repository_names():
            for config in ConfigParser.find(role):
                for service in config.services:
                    if service.name() == service_lang_name:
                        services.extend([PackageManager(cls.env(service), service)])

        return services
