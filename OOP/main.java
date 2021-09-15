import java.text.BreakIterator;
import java.time.LocalDate;

import javax.swing.JOptionPane;

public class main {
    public static void main(String[] args) {
        Integer count = 0;
        String carryOn;
        user user1 = new user();
        user1.idName = 5;

        book book1 = new book();
        book1.id = 5;
        book1.nameBook = "Harry Potter";
        book1.topic = "Adventure";
        book1.editorial = "La granja";
        book1.year = "1998";
        book1.author = "JK Rowling";
        book1.nationality = "British";
        book1.dateBorn = "1980";

        book book2 = new book();
        book2.id = 6;
        book2.nameBook = "Las Aventuras de Guliver";
        book2.topic = "Adventure";
        book2.editorial = "La granja";
        book2.year = "1998";
        book2.author = "Homer Simpson";
        book2.nationality = "British";
        book2.dateBorn = "1985";

        book book3 = new book();
        book3.id = 7;
        book3.nameBook = "La Biblia";
        book3.topic = "Religious";
        book3.editorial = "La granja";
        book3.year = "1978";
        book3.author = "Jhoaquin Phoenix";
        book3.nationality = "American";
        book3.dateBorn = "1975";

        user1.nameUser = JOptionPane.showInputDialog("Type your name..");
        user1.mail = JOptionPane.showInputDialog("Type your email..");
        user1.pass = JOptionPane.showInputDialog("Type your password..");
        while (true) {
            user1.request = JOptionPane.showInputDialog("Type a request book");

            if (book1.nameBook.equals(user1.request)) {
                System.out.println("Congrats " + user1.nameUser + ", your request was on " + book1.loan.now()
                        + " enjoy your loan book " + book1.nameBook + " for 30 days");

                count++;
            } else if (book2.nameBook.equals(user1.request)) {
                System.out.println("Congrats " + user1.nameUser + ", your request was on " + book2.loan.now()
                        + " enjoy your loan book " + book2.nameBook + " for 30 days");
                count++;

            }

            else if (book3.nameBook.equals(user1.request)) {
                System.out.println("Congrats " + user1.nameUser + ", your request was on " + book3.loan.now()
                        + " enjoy your loan book " + book3.nameBook + " for 30 days");

                count++;

            } else {
                System.out.println("We're really sorry, we don't have that book " + user1.request);
            }
            carryOn = JOptionPane.showInputDialog("Do you want to request another book?.. type y or n");
            if (carryOn.equals("n")) {
                break;
            } else {
                System.out.println(count);
            }
            if (count >= 3) {
                System.err.println("You can't to request more books");
                break;
            }

        }
        if (book1.loan.now().compareTo(LocalDate.now()) > 30) {
            System.out.println("Dear " + user1.nameUser + "You loan is in arrears...");

        } else {
            System.out.println("Congrats" + user1.nameUser + "you're a big reader");
        }

    }
}
