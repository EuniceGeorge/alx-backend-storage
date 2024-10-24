#!/usr/bin/env python3

""" simple class with basic redis """
import redis
import uuid
from typing import Union

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
