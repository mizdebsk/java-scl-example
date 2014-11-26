package hello.impl;

import hello.Hello;
import hello.internal.impl.HelloImpl;

public class HelloFactory {
	private static class LazyInitializer {
		static HelloFactory instance = new HelloFactory();
	}

	HelloFactory() {
		// non-public constructor
	}

	public static HelloFactory newInstance() {
		return LazyInitializer.instance;
	}

	public Hello createHello() {
		return new HelloImpl();
	}
}
