package org.example.sysout;

import java.io.IOException;

import org.apache.commons.io.IOUtils;

public class SystemOutputter {
	public static void writeToSysOut(String message) throws IOException {
		IOUtils.write(message + "\n", System.out);
	}
}
