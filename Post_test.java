package com.forumsystem.model;

import javax.persistence.*;
import java.util.Date;
import java.util.List;

@Entity
public class Post {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    private String title;
    private String content;
    private String author;
    private Date timestamp;
    private int likes;

    @OneToMany(mappedBy = "post", cascade = CascadeType.ALL)
    private List<Reply> replies;

    public Post() {
        this.timestamp = new Date();
    }

    // Getters and Setters
    public int getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public String getContent() {
        return content;
    }

    public String getAuthor() {
        return author;
    }

    public Date getTimestamp() {
        return timestamp;
    }

    public int getLikes() {
        return likes;
    }

    public List<Reply> getReplies() {
        return replies;
    }

    public void addReply(Reply reply) {
        replies.add(reply);
    }

    public void addLike() {
        this.likes++;
    }
}
