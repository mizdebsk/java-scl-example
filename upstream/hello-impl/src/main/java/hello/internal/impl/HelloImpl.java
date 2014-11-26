package hello.internal.impl;

import java.io.IOException;

import org.example.sysout.SystemOutputter;

import hello.Hello;

public class HelloImpl implements Hello {

	@Override
	public void hello(String name) {
		try {
			SystemOutputter.writeToSysOut("Hello " + name + "!!!");
		} catch (IOException e) {
			throw new RuntimeException("Freedom of speech was violated", e);
		}
	}

}
