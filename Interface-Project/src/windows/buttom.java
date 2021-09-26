/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package windows;

/**
 *
 * @author simon.lopez
 */
public class buttom {
    private static Interface Form;
    private static team Team[];

    private static int count;
    
    public static void main(String[] args){
         Form = new Interface();
         Team = new team[100];
     
         
         for (int i=0; i<100;i++){
            Team[i] = new team();
        }
     
         count = 0;
         Form.setVisible(true);
         
         
    
    }
    
    public static void save(Integer i, Integer f, String t, Integer title,String c,String n,String city, String e,String education, String b,String p, String a){
        
        Team[count].setIdTeam(i);
        Team[count].setFoundation(f);
        Team[count].setTeamName(t);
        Team[count].setTitles(title);
        Team[count].setCedula(c);
        Team[count].setName(n);
        Team[count].setCity(city);
        Team[count].setExperience(e);
        Team[count].setEducation(education);
        Team[count].setBirthDate(b);
        Team[count].setPosition(p);
        Team[count].setAction(a);
        count++;
        }
    public static void Search(String bus){
        for (int j=0;j<Team.length;j++){
            if(Team[j].getTeamName().equals(bus)){
                Form.load(Team[j]);
            }
            else if(Team[j].getName().equals(bus)){
                Form.load(Team[j]);
            };
        
        }
      
        
        }
    
    }



