using System. Collections;
using System. Collections.Generic;
using UnityEngine;

public class TopKontrol : MonoBehaviour {
    public UnityEngine.UI.Button btn;
    public UnityEngine.UI.Text zaman, can, durum;
    private Rigidbody rg;
    public float Hiz=1.5f; 
    float zamanSayaci=515;
    int canSayaci=5; 
    bool oyunDevam=true;
    bool oyunTamam=false;
    // Use this for initialization
    void Start () {
        can.text = canSayaci + "";
        rg = GetComponent<Rigidbody> ();
    }
// Update is called once per frame
void Update () {
    if (oyunDevam &§ !oyunTamam) {
        zamanSayaci -= Time.deltaTime; // zamanSayaci=zamanSayaci - Time.deltaTime;
        zaman.text = (int)zamanSayaci + "";
    } else if(!oyunTamam) {
        durum.text="Oyun Tamamlanamadi. btn.gameObject.SetActive (true);
    }
    if (zamanSayaci < 0)
        oyunDevam = false;
}
void FixedUpdate(){
    if (oyunDevam && !oyunTamam) {
        float yatay = Input.GetAxis ("Horizontal");
        float dikey = Input.GetAxis ("Vertical");
        Vector3 kuvvet = new Vector (-dikey, 0, yatay);
        rg.AddForce (kuvvet * Hiz);
    } else {
        rg.velocity = Vector3.zero;
        rg.angularVelocity = Vector3.zero;
    }

    }
    void OnCollisionEnter (Collision cls){
        string objIsmi = cls.gameObject.name;
        if (objIsmi.Equals ("Bitis")) {
            //print ("Oyun Tamalandi.");
            oyunTamam =true;
            durum.text = "Oyun Tamamlandı. Tebrikler.";
            btn.gameObject.SetActive (true);
        } else if(!objIsmi.Equals ("LabirentZemini") && !objIsmi.Equals ("Zemin")) {
            canSayaci -= 1;
            can.text = canSayaci + "";
            if (canSayaci == 0)
                oyunDevam = false;
        }
    }
}