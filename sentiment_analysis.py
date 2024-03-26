{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bc8f0442",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-03-26 12:07:38.019 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\HP\\Downloads\\virtual environment\\tahsin_env_1\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "from textblob import TextBlob\n",
    "import pandas as pd\n",
    "import streamlit as st\n",
    "import cleantext\n",
    "\n",
    "\n",
    "st.header('Sentiment Analysis')\n",
    "with st.expander('Analyze Text'):\n",
    "    text = st.text_input('Text here: ')\n",
    "    if text:\n",
    "        blob = TextBlob(text)\n",
    "        st.write('Polarity: ', round(blob.sentiment.polarity,2))\n",
    "        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))\n",
    "\n",
    "\n",
    "    pre = st.text_input('Clean Text: ')\n",
    "    if pre:\n",
    "        st.write(cleantext.clean(pre, clean_all= False, extra_spaces=True ,\n",
    "                                 stopwords=True ,lowercase=True ,numbers=True , punct=True))\n",
    "\n",
    "with st.expander('Analyze CSV'):\n",
    "    upl = st.file_uploader('Upload file')\n",
    "\n",
    "    def score(x):\n",
    "        blob1 = TextBlob(x)\n",
    "        return blob1.sentiment.polarity\n",
    "\n",
    "#\n",
    "    def analyze(x):\n",
    "        if x >= 0.5:\n",
    "            return 'Positive'\n",
    "        elif x <= -0.5:\n",
    "            return 'Negative'\n",
    "        else:\n",
    "            return 'Neutral'\n",
    "\n",
    "#\n",
    "    if upl:\n",
    "        df = pd.read_excel(upl)\n",
    "        del df['Unnamed: 0']\n",
    "        df['score'] = df['tweets'].apply(score)\n",
    "        df['analysis'] = df['score'].apply(analyze)\n",
    "        st.write(df.head(10))\n",
    "\n",
    "        @st.cache\n",
    "        def convert_df(df):\n",
    "            # IMPORTANT: Cache the conversion to prevent computation on every rerun\n",
    "            return df.to_csv().encode('utf-8')\n",
    "\n",
    "        csv = convert_df(df)\n",
    "\n",
    "        st.download_button(\n",
    "            label=\"Download data as CSV\",\n",
    "            data=csv,\n",
    "            file_name='sentiment.csv',\n",
    "            mime='text/csv',\n",
    "        )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "tahsin-1",
   "language": "python",
   "name": "tahsin-1"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
