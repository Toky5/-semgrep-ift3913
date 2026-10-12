class Comparaisons {

    static final String ADMIN = "admin";

    boolean cas1(String role) { return role == ADMIN; }
    boolean cas2(String role) { return role==ADMIN; }
    // role == ADMIN
    boolean cas4(int n)       { return n == 2; }
    boolean cas5(String role) { return ADMIN == role; }
}
