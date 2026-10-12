class Exemple1Test {

    static final String ADMIN = "admin";

    boolean cas(String role, int n) {
        // ruleid: string-comparee-avec-egal-egal
        if (role == ADMIN) return true;
        // ruleid: string-comparee-avec-egal-egal
        if ("admin" == role) return true;
        // ok: string-comparee-avec-egal-egal
        if (role.equals(ADMIN)) return true;
        // ok: string-comparee-avec-egal-egal
        if (role == null) return false;
        // ok: string-comparee-avec-egal-egal
        if (n == 2) return false;
        return false;
    }
}
