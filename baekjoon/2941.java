import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        String[] list = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        for (String s : list) {
            input = input.replace(s, "!");
        }
        System.out.println(input.length());
    }
}
