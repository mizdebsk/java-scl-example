package com.example.welcome.impl;

import hello.Hello;
import hello.impl.HelloFactory;

import com.example.welcome.IWelcome;

public class Welcome implements IWelcome {

	private static final HelloFactory HELLO_FACTORY;

	private final Hello hello;

	static {
		HELLO_FACTORY = HelloFactory.newInstance();
	}

	public Welcome() {
		hello = HELLO_FACTORY.createHello();
	}

	@Override
	public void welcome() {
		hello.hello(SOFTWARE_COLLECTION);
	}

}
