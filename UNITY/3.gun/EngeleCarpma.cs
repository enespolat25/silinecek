using System.Collections;
using System.Collections.Generic;
using UnityEngine;



public class EngeleCarpma : MonoBehaviour
{
    AudioSource audioSource;
    
    // Start is called before the first frame update
    void Start()
    {
        audioSource = GetComponent<AudioSource>();
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private void OnCollisionEnter(Collision collision)
    {
        if(collision.collider.tag=="Engel")
        {
            audioSource.Play();
            print(collision.collider.tag);

        }
        print(collision.collider.tag);
    }
}
