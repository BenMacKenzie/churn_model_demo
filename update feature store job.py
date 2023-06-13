# Databricks notebook source
from features.feature_generation import build_feature_table
build_feature_table('customer_service_calls', drop_existing=False, update=True)
build_feature_table('customer_service_calls', drop_existing=False, update=True)

