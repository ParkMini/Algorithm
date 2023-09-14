import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next().toLowerCase();

        int[] alphabetCount = new int[26];
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (Character.isLetter(c)) {
                int index = c - 'a';
                alphabetCount[index]++;
            }
        }

        int maxCount = 0;
        char mostFrequentChar = '?';
        for (int i = 0; i < 26; i++) {
            if (alphabetCount[i] > maxCount) {
                maxCount = alphabetCount[i];
                mostFrequentChar = (char) ('A' + i);
            } else if (alphabetCount[i] == maxCount) {
                mostFrequentChar = '?';
            }
        }
        System.out.println(mostFrequentChar);
    }
}
