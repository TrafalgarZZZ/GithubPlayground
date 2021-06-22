package utils;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class UtilityTest {

    @Test
    public void sum() {
        assertEquals(10 + 25, Utility.sum(10, 25));
    }
}