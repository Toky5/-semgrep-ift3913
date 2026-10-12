public class Login {

    static final String ADMIN = "admin";

    static boolean estAdmin(String role) {
        return role == ADMIN;
    }

    public static void main(String[] args) {
        String saisie = new StringBuilder("ad").append("min").toString();

        assert estAdmin("admin");
        System.out.println("Test avec \"admin\" : OK");

        assert estAdmin(saisie) : "estAdmin(saisie) devrait renvoyer true";
        System.out.println("Test avec la saisie : OK");
    }
}