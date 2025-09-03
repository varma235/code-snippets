public class Snippet {

    // --- Feature: Factorial Calculator ---
    public static long factorial(int n) {
        if (n < 0) throw new IllegalArgumentException("Negative numbers not allowed!")
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    // --- Demo run ---
    public static void main(String[] args) {
        System.out.println("🧮 Factorial of 5: " + factorial(5));
    }
}
