package jejbsample;

import java.io.Serializable;

public class Employee implements Serializable{
    @SuppressWarnings("compatibility:3768358876852373119")
    private static final long serialVersionUID = 1L;
    private String empName;
    private String empNo;
    private String empDept;
    private String empLoc;
    
    
    public Employee() {
        super();
    }

    public void setEmpName(String empName) {
        this.empName = empName;
    }

    public String getEmpName() {
        return empName;
    }

    public void setEmpNo(String empNo) {
        this.empNo = empNo;
    }

    public String getEmpNo() {
        return empNo;
    }

    public void setEmpDept(String empDept) {
        this.empDept = empDept;
    }

    public String getEmpDept() {
        return empDept;
    }

    public void setEmpLoc(String empLoc) {
        this.empLoc = empLoc;
    }

    public String getEmpLoc() {
        return empLoc;
    }
}
