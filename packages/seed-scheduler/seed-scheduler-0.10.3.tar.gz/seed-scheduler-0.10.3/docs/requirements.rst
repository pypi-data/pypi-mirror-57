============
Requirements
============

Overview
========

The Seed Scheduler requires the following dependencies to run:

* Python 3.6
* PostgreSQL >= 9.3
* Redis >= 2.10 or RabbitMQ >= 3.4 as the Celery Broker

Python requirements
===================

The full list of Python packages required are detailed in the project's
setup.py file, but the major ones are:

* Django 1.9
* Django REST Framework 3.3
* Celery 3.1

.. note::

    A celery worker needs to be running to process post-save tasks and
    scheduled metric firing tasks.

Seed Requirements
=================

The Seed Scheduler only depends on one other seed service, the
`Go Metrics API`_.

.. _Go Metrics API: https://github.com/praekelt/go-metrics-api
