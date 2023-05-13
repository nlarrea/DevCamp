import React from 'react';

export const JournalEntry = props => {
    return (
        <div>
            <h1>{props.title}</h1>
            <p>{props.content}</p>
        </div>
    )
}