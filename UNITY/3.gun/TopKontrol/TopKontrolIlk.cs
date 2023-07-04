using System.Collections;
using System. Collections.Generic;
using UnityEngine;
public class TopKontrol : MonoBehaviour {
    private Rigidbody rg; 
    public float Hiz=1.5f;
    // Use this for initialization
    void Start () {
        rg = GetComponent<Rigidbody>();
    }
  
    void FixedUpdate(){
            float yatay = Input.GetAxis("Horizontal");
            float dikey = Input.GetAxis("Vertical");
            Vector3 kuvvet = new Vector(-dikey,o, yatay);
            rg. AddForce (kuvvet*Hiz) ;
        }
}