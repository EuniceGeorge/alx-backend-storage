#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" simple class with basic redis """
import redis
import uuid
from typing import Union, Callable, Optional

class Cache:
    def __init__(self):
        """
        Initialize the Cache instance with a Redis client.
        Flushes the database upon initialization.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data:Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a randomly generated key.
        
        Args:
            data: The data to store in Redis
            
        Returns:
            str: The randomly generated key used to store the data
        """
        # Generate a random key using uuid4
        key = str(uuid.uuid4())
        
        # Store the data in Redis
        self._redis.set(key, data)
        
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """get data"""
        data = self._redis.get(key)
        if fn is not None:
            data = fn(data)
        return data
    
    def get_str(self, key: str) -> str:
        """get_str"""
        return self.get(key, fn=str)
    
    def get_int(self, key: int) -> int:
        """get_int"""
        return self.get(key, fn=int)
